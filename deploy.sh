#!/bin/bash

# ClassBuddy Production Deployment Script
# This script automates the deployment process for ClassBuddy

set -e  # Exit on any error

# Configuration
PROJECT_NAME="classbuddy"
REGISTRY="ghcr.io"
IMAGE_NAME="$REGISTRY/jani-shiv/$PROJECT_NAME"
VERSION=${1:-"latest"}
ENVIRONMENT=${2:-"production"}

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

warn() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] WARNING: $1${NC}"
}

error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] ERROR: $1${NC}"
    exit 1
}

check_prerequisites() {
    log "Checking prerequisites..."
    
    # Check if required tools are installed
    command -v docker >/dev/null 2>&1 || error "Docker is required but not installed"
    command -v docker-compose >/dev/null 2>&1 || warn "Docker Compose not found, using docker compose"
    
    # Check environment variables
    if [ "$ENVIRONMENT" = "production" ]; then
        [ -z "$DATABASE_URL" ] && error "DATABASE_URL environment variable is required"
        [ -z "$SECRET_KEY" ] && error "SECRET_KEY environment variable is required"
        [ -z "$REDIS_URL" ] && warn "REDIS_URL not set, using default"
    fi
    
    log "Prerequisites check completed"
}

build_image() {
    log "Building Docker image..."
    
    # Build the image with version tag
    docker build \
        --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
        --build-arg VCS_REF=$(git rev-parse --short HEAD) \
        --build-arg VERSION=$VERSION \
        -t $IMAGE_NAME:$VERSION \
        -t $IMAGE_NAME:latest \
        .
    
    log "Docker image built successfully"
}

run_tests() {
    log "Running tests..."
    
    # Run backend tests
    docker run --rm \
        -e DATABASE_URL="sqlite:///./test.db" \
        -e SECRET_KEY="test-secret" \
        $IMAGE_NAME:$VERSION \
        python -m pytest tests/ -v
    
    log "Tests completed successfully"
}

deploy_to_docker_compose() {
    log "Deploying with Docker Compose..."
    
    # Export environment variables for docker-compose
    export IMAGE_TAG=$VERSION
    export ENVIRONMENT=$ENVIRONMENT
    
    # Deploy using docker-compose
    if command -v docker-compose >/dev/null 2>&1; then
        docker-compose -f docker-compose.yml -f docker-compose.$ENVIRONMENT.yml up -d
    else
        docker compose -f docker-compose.yml -f docker-compose.$ENVIRONMENT.yml up -d
    fi
    
    log "Deployment completed"
}

deploy_to_kubernetes() {
    log "Deploying to Kubernetes..."
    
    # Check if kubectl is available
    command -v kubectl >/dev/null 2>&1 || error "kubectl is required for Kubernetes deployment"
    
    # Apply Kubernetes manifests
    envsubst < k8s/namespace.yaml | kubectl apply -f -
    envsubst < k8s/configmap.yaml | kubectl apply -f -
    envsubst < k8s/secret.yaml | kubectl apply -f -
    envsubst < k8s/deployment.yaml | kubectl apply -f -
    envsubst < k8s/service.yaml | kubectl apply -f -
    envsubst < k8s/ingress.yaml | kubectl apply -f -
    
    # Wait for rollout to complete
    kubectl rollout status deployment/$PROJECT_NAME -n $PROJECT_NAME
    
    log "Kubernetes deployment completed"
}

deploy_to_aws() {
    log "Deploying to AWS ECS..."
    
    # Check AWS CLI
    command -v aws >/dev/null 2>&1 || error "AWS CLI is required"
    
    # Login to ECR
    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
    
    # Tag image for ECR
    ECR_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$PROJECT_NAME"
    docker tag $IMAGE_NAME:$VERSION $ECR_URI:$VERSION
    docker tag $IMAGE_NAME:$VERSION $ECR_URI:latest
    
    # Push to ECR
    docker push $ECR_URI:$VERSION
    docker push $ECR_URI:latest
    
    # Update ECS service
    aws ecs update-service \
        --cluster $ECS_CLUSTER \
        --service $PROJECT_NAME \
        --force-new-deployment
    
    log "AWS ECS deployment completed"
}

deploy_to_gcp() {
    log "Deploying to Google Cloud Run..."
    
    # Check gcloud CLI
    command -v gcloud >/dev/null 2>&1 || error "gcloud CLI is required"
    
    # Build and push to Container Registry
    gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/$PROJECT_NAME:$VERSION
    
    # Deploy to Cloud Run
    gcloud run deploy $PROJECT_NAME \
        --image gcr.io/$GCP_PROJECT_ID/$PROJECT_NAME:$VERSION \
        --platform managed \
        --region $GCP_REGION \
        --allow-unauthenticated \
        --set-env-vars="DATABASE_URL=$DATABASE_URL,SECRET_KEY=$SECRET_KEY"
    
    log "Google Cloud Run deployment completed"
}

health_check() {
    log "Performing health check..."
    
    # Wait for service to be ready
    sleep 30
    
    # Check health endpoint
    if [ "$DEPLOYMENT_TYPE" = "docker-compose" ]; then
        HEALTH_URL="http://localhost:8000/health"
    elif [ "$DEPLOYMENT_TYPE" = "kubernetes" ]; then
        HEALTH_URL="http://$(kubectl get service $PROJECT_NAME -n $PROJECT_NAME -o jsonpath='{.status.loadBalancer.ingress[0].ip}'):80/health"
    else
        warn "Health check not configured for $DEPLOYMENT_TYPE"
        return
    fi
    
    for i in {1..10}; do
        if curl -f $HEALTH_URL > /dev/null 2>&1; then
            log "Health check passed"
            return
        fi
        warn "Health check attempt $i failed, retrying..."
        sleep 10
    done
    
    error "Health check failed after 10 attempts"
}

cleanup() {
    log "Cleaning up old images..."
    
    # Remove old images (keep last 3 versions)
    docker images $IMAGE_NAME --format "table {{.Tag}}\t{{.CreatedAt}}" | \
    tail -n +2 | sort -k2 -r | tail -n +4 | awk '{print $1}' | \
    while read tag; do
        if [ "$tag" != "latest" ] && [ "$tag" != "$VERSION" ]; then
            docker rmi $IMAGE_NAME:$tag || true
        fi
    done
    
    log "Cleanup completed"
}

rollback() {
    log "Rolling back to previous version..."
    
    case $DEPLOYMENT_TYPE in
        "docker-compose")
            docker-compose down
            docker-compose up -d
            ;;
        "kubernetes")
            kubectl rollout undo deployment/$PROJECT_NAME -n $PROJECT_NAME
            ;;
        "aws")
            # AWS ECS rollback would need previous task definition ARN
            warn "Manual rollback required for AWS ECS"
            ;;
        "gcp")
            # Cloud Run rollback to previous revision
            gcloud run services replace-traffic $PROJECT_NAME --to-revisions=LATEST:0,$(gcloud run revisions list --service=$PROJECT_NAME --limit=1 --sort-by=~metadata.creationTimestamp --format="value(metadata.name)" | tail -1):100
            ;;
    esac
    
    log "Rollback completed"
}

# Main execution
main() {
    log "Starting ClassBuddy deployment (Version: $VERSION, Environment: $ENVIRONMENT)"
    
    # Determine deployment type from environment variable or argument
    DEPLOYMENT_TYPE=${DEPLOYMENT_TYPE:-${3:-"docker-compose"}}
    
    check_prerequisites
    
    if [ "$SKIP_BUILD" != "true" ]; then
        build_image
    fi
    
    if [ "$SKIP_TESTS" != "true" ]; then
        run_tests
    fi
    
    case $DEPLOYMENT_TYPE in
        "docker-compose")
            deploy_to_docker_compose
            ;;
        "kubernetes"|"k8s")
            deploy_to_kubernetes
            ;;
        "aws")
            deploy_to_aws
            ;;
        "gcp")
            deploy_to_gcp
            ;;
        *)
            error "Unknown deployment type: $DEPLOYMENT_TYPE"
            ;;
    esac
    
    health_check
    cleanup
    
    log "Deployment completed successfully!"
    log "Application is available at the configured endpoint"
}

# Handle script arguments
case "${1:-}" in
    "rollback")
        rollback
        exit 0
        ;;
    "health")
        health_check
        exit 0
        ;;
    "build")
        build_image
        exit 0
        ;;
    "test")
        run_tests
        exit 0
        ;;
    *)
        main "$@"
        ;;
esac

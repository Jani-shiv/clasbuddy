from pydantic_settings import BaseSettings
from typing import List, Optional
import os


class Settings(BaseSettings):
    # Database
    database_url: str = "sqlite:///./classbuddy.db"
    
    # Authentication
    secret_key: str = "your-super-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # AI/LLM
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    refact_ai_api_key: Optional[str] = None
    
    # Redis
    redis_url: str = "redis://localhost:6379/0"
    
    # Monitoring
    sentry_dsn: Optional[str] = None
    log_level: str = "INFO"
    environment: str = "development"
    
    # CORS
    allowed_origins: List[str] = ["http://localhost:3000", "http://localhost:8081"]
    
    # Rate Limiting
    rate_limit_enabled: bool = True
    rate_limit_requests_per_minute: int = 60
    
    # Push Notifications
    fcm_server_key: Optional[str] = None
    apns_team_id: Optional[str] = None
    apns_key_id: Optional[str] = None
    apns_private_key_path: Optional[str] = None
    
    class Config:
        env_file = ".env"


settings = Settings()

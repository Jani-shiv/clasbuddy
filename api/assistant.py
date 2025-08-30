from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional, Dict, Any
from models.user import User
from auth.authentication import get_current_active_user
from services.ai_service import ai_manager
from utils.helpers import simple_nlp_response
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str
    context: Optional[str] = None
    provider: Optional[str] = None


class DocumentAnalysisRequest(BaseModel):
    content: str
    provider: Optional[str] = None


class SummarizationRequest(BaseModel):
    text: str
    max_length: int = 200
    provider: Optional[str] = None


class AIResponse(BaseModel):
    answer: str
    provider_used: Optional[str] = None
    confidence: Optional[float] = None


class DocumentAnalysisResponse(BaseModel):
    summary: str
    key_points: list = []
    themes: list = []
    recommendations: list = []


@router.post("/ask", response_model=AIResponse)
async def ask_question(
    request: QuestionRequest,
    current_user: User = Depends(get_current_active_user)
):
    """Ask a question to the AI assistant"""
    try:
        # Try AI first if available
        if ai_manager.providers:
            answer = await ai_manager.answer_question(
                question=request.question,
                context=request.context,
                provider=request.provider
            )
            provider_used = request.provider or ai_manager.default_provider
            return AIResponse(
                answer=answer,
                provider_used=provider_used,
                confidence=0.8
            )
        else:
            # Fallback to simple NLP
            answer = simple_nlp_response(request.question)
            return AIResponse(
                answer=answer,
                provider_used="simple_nlp",
                confidence=0.3
            )
    
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        # Fallback to simple response
        answer = simple_nlp_response(request.question)
        return AIResponse(
            answer=answer,
            provider_used="fallback",
            confidence=0.2
        )


@router.post("/analyze-document", response_model=DocumentAnalysisResponse)
async def analyze_document(
    request: DocumentAnalysisRequest,
    current_user: User = Depends(get_current_active_user)
):
    """Analyze a document using AI"""
    try:
        if not ai_manager.providers:
            raise HTTPException(
                status_code=503,
                detail="AI services not available"
            )
        
        analysis = await ai_manager.analyze_document(
            content=request.content,
            provider=request.provider
        )
        
        return DocumentAnalysisResponse(
            summary=analysis.get("summary", ""),
            key_points=analysis.get("key_points", analysis.get("key_info", [])),
            themes=analysis.get("themes", analysis.get("topics", [])),
            recommendations=analysis.get("recommendations", analysis.get("actions", []))
        )
    
    except Exception as e:
        logger.error(f"Error analyzing document: {e}")
        raise HTTPException(
            status_code=500,
            detail="Document analysis failed"
        )


@router.post("/summarize", response_model=AIResponse)
async def summarize_text(
    request: SummarizationRequest,
    current_user: User = Depends(get_current_active_user)
):
    """Summarize text using AI"""
    try:
        if not ai_manager.providers:
            raise HTTPException(
                status_code=503,
                detail="AI services not available"
            )
        
        summary = await ai_manager.summarize_text(
            text=request.text,
            max_length=request.max_length,
            provider=request.provider
        )
        
        provider_used = request.provider or ai_manager.default_provider
        return AIResponse(
            answer=summary,
            provider_used=provider_used,
            confidence=0.9
        )
    
    except Exception as e:
        logger.error(f"Error summarizing text: {e}")
        raise HTTPException(
            status_code=500,
            detail="Text summarization failed"
        )


@router.get("/providers")
async def get_available_providers(
    current_user: User = Depends(get_current_active_user)
):
    """Get list of available AI providers"""
    return {
        "providers": list(ai_manager.providers.keys()),
        "default": ai_manager.default_provider,
        "count": len(ai_manager.providers)
    }


@router.post("/chat")
async def chat_with_ai(
    request: QuestionRequest,
    current_user: User = Depends(get_current_active_user)
):
    """Enhanced chat interface with AI"""
    try:
        # Add user context to the conversation
        enhanced_context = f"""
        User Information:
        - Name: {current_user.full_name or current_user.username}
        - Student ID: {current_user.student_id or 'Not provided'}
        - Year: {current_user.year or 'Not specified'}
        - Major: {current_user.major or 'Not specified'}
        
        Additional Context: {request.context or 'None'}
        """
        
        if ai_manager.providers:
            answer = await ai_manager.answer_question(
                question=request.question,
                context=enhanced_context,
                provider=request.provider
            )
            return {
                "response": answer,
                "type": "ai_powered",
                "user_context_used": True
            }
        else:
            answer = simple_nlp_response(request.question)
            return {
                "response": answer,
                "type": "rule_based",
                "user_context_used": False
            }
    
    except Exception as e:
        logger.error(f"Error in chat: {e}")
        answer = simple_nlp_response(request.question)
        return {
            "response": answer,
            "type": "fallback",
            "error": str(e)
        }

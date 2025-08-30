import openai
import anthropic
import asyncio
import logging
from typing import Dict, List, Optional, Any
from pydantic import BaseModel
from config import settings

logger = logging.getLogger(__name__)


class AIProvider:
    """Base class for AI providers"""
    
    async def generate_response(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError
    
    async def analyze_document(self, content: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError
    
    async def summarize_text(self, text: str, **kwargs) -> str:
        raise NotImplementedError


class OpenAIProvider(AIProvider):
    """OpenAI GPT provider"""
    
    def __init__(self, api_key: str):
        self.client = openai.AsyncOpenAI(api_key=api_key)
    
    async def generate_response(
        self, 
        prompt: str, 
        model: str = "gpt-4",
        max_tokens: int = 1000,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """Generate response using OpenAI GPT"""
        try:
            response = await self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise
    
    async def analyze_document(self, content: str, **kwargs) -> Dict[str, Any]:
        """Analyze document content"""
        prompt = f"""
        Analyze the following document and provide:
        1. A brief summary
        2. Key topics/themes
        3. Important information
        4. Actionable items (if any)
        
        Document:
        {content}
        
        Please format your response as JSON with keys: summary, topics, key_info, actions
        """
        
        response = await self.generate_response(prompt, **kwargs)
        try:
            import json
            return json.loads(response)
        except json.JSONDecodeError:
            return {"summary": response, "topics": [], "key_info": [], "actions": []}
    
    async def summarize_text(self, text: str, max_length: int = 200, **kwargs) -> str:
        """Summarize text content"""
        prompt = f"""
        Summarize the following text in {max_length} characters or less:
        
        {text}
        """
        return await self.generate_response(prompt, max_tokens=max_length//4, **kwargs)


class AnthropicProvider(AIProvider):
    """Anthropic Claude provider"""
    
    def __init__(self, api_key: str):
        self.client = anthropic.AsyncAnthropic(api_key=api_key)
    
    async def generate_response(
        self,
        prompt: str,
        model: str = "claude-3-sonnet-20240229",
        max_tokens: int = 1000,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """Generate response using Claude"""
        try:
            response = await self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.content[0].text
        except Exception as e:
            logger.error(f"Anthropic API error: {e}")
            raise
    
    async def analyze_document(self, content: str, **kwargs) -> Dict[str, Any]:
        """Analyze document using Claude"""
        prompt = f"""
        Please analyze this document and provide structured insights:
        
        {content}
        
        Format your response as JSON with:
        - summary: Brief overview
        - key_points: Important information
        - themes: Main topics
        - recommendations: Suggested actions
        """
        
        response = await self.generate_response(prompt, **kwargs)
        try:
            import json
            return json.loads(response)
        except json.JSONDecodeError:
            return {"summary": response, "key_points": [], "themes": [], "recommendations": []}
    
    async def summarize_text(self, text: str, max_length: int = 200, **kwargs) -> str:
        """Summarize text using Claude"""
        prompt = f"""
        Create a concise summary of this text (max {max_length} characters):
        
        {text}
        """
        return await self.generate_response(prompt, max_tokens=max_length//4, **kwargs)


class AIManager:
    """AI service manager that handles multiple providers"""
    
    def __init__(self):
        self.providers: Dict[str, AIProvider] = {}
        self.default_provider = None
        
        # Initialize providers based on available API keys
        if settings.openai_api_key:
            self.providers["openai"] = OpenAIProvider(settings.openai_api_key)
            if not self.default_provider:
                self.default_provider = "openai"
        
        if settings.anthropic_api_key:
            self.providers["anthropic"] = AnthropicProvider(settings.anthropic_api_key)
            if not self.default_provider:
                self.default_provider = "anthropic"
        
        if not self.providers:
            logger.warning("No AI providers configured - AI features will be disabled")
    
    def get_provider(self, provider_name: Optional[str] = None) -> AIProvider:
        """Get AI provider by name or default"""
        if not self.providers:
            raise ValueError("No AI providers available")
        
        provider_name = provider_name or self.default_provider
        if provider_name not in self.providers:
            raise ValueError(f"Provider {provider_name} not available")
        
        return self.providers[provider_name]
    
    async def generate_response(
        self, 
        prompt: str, 
        provider: Optional[str] = None,
        **kwargs
    ) -> str:
        """Generate AI response"""
        ai_provider = self.get_provider(provider)
        return await ai_provider.generate_response(prompt, **kwargs)
    
    async def analyze_document(
        self,
        content: str,
        provider: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Analyze document with AI"""
        ai_provider = self.get_provider(provider)
        return await ai_provider.analyze_document(content, **kwargs)
    
    async def summarize_text(
        self,
        text: str,
        provider: Optional[str] = None,
        **kwargs
    ) -> str:
        """Summarize text with AI"""
        ai_provider = self.get_provider(provider)
        return await ai_provider.summarize_text(text, **kwargs)
    
    async def answer_question(
        self,
        question: str,
        context: Optional[str] = None,
        provider: Optional[str] = None,
        **kwargs
    ) -> str:
        """Answer question with optional context"""
        if context:
            prompt = f"""
            Context: {context}
            
            Question: {question}
            
            Please provide a helpful and accurate answer based on the context provided.
            """
        else:
            prompt = f"""
            Question: {question}
            
            Please provide a helpful and accurate answer.
            """
        
        return await self.generate_response(prompt, provider, **kwargs)


# Global AI manager instance
ai_manager = AIManager()

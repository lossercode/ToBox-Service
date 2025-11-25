"""LLM schemas"""
from pydantic import BaseModel, ConfigDict
from typing import Optional


class ChatRequest(BaseModel):
    """Chat request schema"""
    message: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 200
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "请简单解释一下什么是AI大模型",
                "temperature": 0.7,
                "max_tokens": 200
            }
        }
    )


class ChatResponse(BaseModel):
    """Chat response schema"""
    message: str
    model: str = "kimi-k2-0905"
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "AI大模型是指...",
                "model": "kimi-k2-0905"
            }
        }
    )

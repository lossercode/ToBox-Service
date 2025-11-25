"""LLM API endpoints"""

from fastapi import APIRouter, HTTPException
from app.schemas.llm import ChatRequest, ChatResponse
from app.services.llm import llm_service
from app.utils.logger import logger

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    LLM 聊天接口
    
    Args:
        request: 聊天请求，包含用户消息和参数
        
    Returns:
        ChatResponse: 包含 LLM 回复的响应
        
    Raises:
        HTTPException: 当 LLM 服务调用失败时返回 500 错误
    """
    try:
        logger.info(f"收到聊天请求: {request.message}")
        
        # 调用 LLM 服务
        reply = llm_service.chat(
            message=request.message,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        # 返回响应对象
        return ChatResponse(message=reply, model="kimi-k2-0905")
        
    except Exception as e:
        logger.error(f"聊天接口错误: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"LLM 服务错误: {str(e)}"
        )

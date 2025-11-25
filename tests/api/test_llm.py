"""Tests for LLM endpoints"""
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock


def test_chat_success(client: TestClient):
    """Test successful chat request"""
    
    # Mock the LLM service response
    with patch('app.services.llm.llm_service.chat') as mock_chat:
        mock_chat.return_value = "这是一个模拟的 LLM 回复"
        
        response = client.post(
            "/api/v1/llm/chat",
            json={
                "message": "你好，请介绍一下自己",
                "temperature": 0.7,
                "max_tokens": 200
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "这是一个模拟的 LLM 回复"
        assert data["model"] == "kimi-k2-0905"
        
        # Verify the service was called with correct parameters
        mock_chat.assert_called_once_with(
            message="你好，请介绍一下自己",
            temperature=0.7,
            max_tokens=200
        )


def test_chat_with_default_parameters(client: TestClient):
    """Test chat request with default parameters"""
    
    with patch('app.services.llm.llm_service.chat') as mock_chat:
        mock_chat.return_value = "默认参数的回复"
        
        response = client.post(
            "/api/v1/llm/chat",
            json={"message": "简单问题"}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "默认参数的回复"
        
        # Verify default parameters were used
        mock_chat.assert_called_once_with(
            message="简单问题",
            temperature=0.7,
            max_tokens=200
        )


def test_chat_service_error(client: TestClient):
    """Test chat request when service fails"""
    
    with patch('app.services.llm.llm_service.chat') as mock_chat:
        mock_chat.side_effect = Exception("API 连接失败")
        
        response = client.post(
            "/api/v1/llm/chat",
            json={"message": "测试消息"}
        )
        
        assert response.status_code == 500
        data = response.json()
        assert "LLM 服务错误" in data["detail"]


def test_chat_invalid_request(client: TestClient):
    """Test chat request with invalid data"""
    
    # Missing required 'message' field
    response = client.post(
        "/api/v1/llm/chat",
        json={"temperature": 0.5}
    )
    
    assert response.status_code == 422  # Validation error


def test_chat_response_schema(client: TestClient):
    """Test that response matches ChatResponse schema"""
    
    with patch('app.services.llm.llm_service.chat') as mock_chat:
        mock_chat.return_value = "完整的回复内容"
        
        response = client.post(
            "/api/v1/llm/chat",
            json={"message": "测试"}
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response has required fields
        assert "message" in data
        assert "model" in data
        assert isinstance(data["message"], str)
        assert isinstance(data["model"], str)

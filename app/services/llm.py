"""LLM Service - 与大模型 API 交互"""

import requests
from typing import Optional
from app.utils.logger import logger


class LLMService:
    """LLM 服务类"""
    
    def __init__(self):
        """初始化 LLM 服务"""
        self.url = "https://apis.iflow.cn/v1/chat/completions"
        self.headers = {
            "Authorization": "Bearer sk-ead8f7f745d65aeb099e0e47c54538e7",
            "Content-Type": "application/json"
        }
        self.model = "kimi-k2-0905"
    
    def chat(
        self, 
        message: str, 
        temperature: Optional[float] = 0.7,
        max_tokens: Optional[int] = 200
    ) -> str:
        """
        与 LLM 进行对话
        
        Args:
            message: 用户消息
            temperature: 温度参数（0-1），控制输出的随机性
            max_tokens: 最大生成 token 数
            
        Returns:
            LLM 的回复消息
            
        Raises:
            Exception: 当 API 调用失败时抛出异常
        """
        try:
            # 构建请求数据
            data = {
                "model": self.model,
                "messages": [
                    {"role": "user", "content": message}
                ],
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            
            logger.info(f"发送 LLM 请求: {message[:50]}...")
            
            # 发起请求
            response = requests.post(
                self.url, 
                json=data, 
                headers=self.headers,
                timeout=30
            )
            
            # 检查响应状态
            response.raise_for_status()
            
            # 解析响应
            result = response.json()
            
            # 提取回复内容
            reply = result["choices"][0]["message"]["content"]
            
            logger.info(f"LLM 回复成功: {reply[:50]}...")
            
            return reply
            
        except requests.exceptions.RequestException as e:
            logger.error(f"LLM API 请求失败: {str(e)}")
            raise Exception(f"LLM API 请求失败: {str(e)}")
        except (KeyError, IndexError) as e:
            logger.error(f"LLM 响应格式错误: {str(e)}")
            raise Exception(f"LLM 响应格式错误: {str(e)}")
        except Exception as e:
            logger.error(f"未知错误: {str(e)}")
            raise Exception(f"未知错误: {str(e)}")


# 创建全局 LLM 服务实例
llm_service = LLMService()

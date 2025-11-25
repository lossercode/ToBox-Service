"""Application configuration"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""
    
    # Project info
    PROJECT_NAME: str = "ToBox Service"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "A FastAPI service for ToBox"
    
    # API settings
    API_V1_STR: str = "/api/v1"
    
    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # CORS settings
    BACKEND_CORS_ORIGINS: list = ["*"]
    
    # Database settings (for future use)
    DATABASE_URL: Optional[str] = None
    
    # Redis settings (for future use)
    REDIS_URL: Optional[str] = None
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()

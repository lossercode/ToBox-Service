"""Hello schemas"""

from pydantic import BaseModel, ConfigDict


class HelloResponse(BaseModel):
    """Hello response schema"""
    message: str
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Hello, World!"
            }
        }
    )

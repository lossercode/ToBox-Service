"""Hello endpoints"""
from fastapi import APIRouter
from app.schemas.hello import HelloResponse

router = APIRouter()


@router.get("", response_model=HelloResponse)
async def hello():
    """Simple hello endpoint"""
    return HelloResponse(message="Hello, World!")


@router.get("/{name}", response_model=HelloResponse)
async def hello_name(name: str):
    """Hello endpoint with name parameter"""
    return HelloResponse(message=f"Hello, {name}!")

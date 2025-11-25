"""API v1 module"""
from fastapi import APIRouter
from app.api.v1 import hello

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(hello.router, prefix="/hello", tags=["hello"])

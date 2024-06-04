from fastapi import APIRouter, status
from pydantic import BaseModel

## define the health router
health_router = APIRouter()

## creat a base model 
class HealthCheck(BaseModel):
    """Health Check Response"""
    status: str

## define the health check endpoint
@health_router.get("/health", 
                   tags= ["health"],
                   summary = "Health Check",
                   response_description="Health Check Response",
                   status_code= status.HTTP_200_OK,
                   response_model = HealthCheck)
async def health_check():
    """Health Check"""
    return HealthCheck(status = "ok")


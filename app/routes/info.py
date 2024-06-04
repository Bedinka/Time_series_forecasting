from fastapi import APIRouter, status
from pydantic import BaseModel

## define the info router
info_router = APIRouter()

## creat a base model 
class APIInfo(BaseModel):
    """API Information"""
    title: str
    description: str
    version: str

## define the info endpoint
@info_router.get("/info", 
                 tags= ["info"],
                 summary = "API Information",
                 response_description="API Information",
                 status_code= status.HTTP_200_OK,
                 response_model = APIInfo)
async def api_info():
    """API Information"""
    return APIInfo(title = "My API", 
                   description = "This is a very fancy API", 
                   version = "0.0.1")

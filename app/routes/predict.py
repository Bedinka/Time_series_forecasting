from fastapi import APIRouter, status
from app.models.request.request_model import PredictionRequest
from app.models.response.response_model import PredictionResponse
from app.models.prediction_status.prediction_status import PredictionStatus
import numpy as np 
import uuid 
import time 

## define the predicty router
predict_router = APIRouter()

## define the prediction endpoint
@predict_router.post("/predict",
                     tags=["predict_endpoint"],
                     summary="Make a prediction",
                     response_description="Prediction Response",
                     status_code=status.HTTP_200_OK,
                     response_model=PredictionResponse)

async def predict(input_data: PredictionRequest, response_model=PredictionResponse):
    """Make a prediction"""
    ## perform the prediction here 
    ## .... 
    ## ....
    ## ....
    ## ....
    return PredictionResponse(
        prediction_results = np.array([1, 2, 3]),
        prediction_id = str(uuid.uuid4()),
        prediction_status = PredictionStatus.completed.value,
        prediction_timestamp = str(time.time()),
        request_id = str(uuid.uuid4()) ## to be replaced with actual request id
    )

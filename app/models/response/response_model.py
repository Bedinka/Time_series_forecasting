from pydantic import BaseModel, Field
from typing import List, Dict, Any

class PredictionResponse(BaseModel):
    """Prediction Response"""
    prediction_results: List[Dict[str, Any]] = Field(..., description="A list of dictionaries containing the timestamps and their forecasted values.")
    prediction_id: str = Field(..., example="pred_12345")
    prediction_status: str = Field(..., example="completed")
    prediction_timestamp: str = Field(..., example="2023-01-01T00:00:00Z")
    request_id: str = Field(..., example="req_67890")

    class Config:
        schema_extra = {
            "example": {
                "prediction_results": [
                    {"timestamp": "2023-01-01T01:00:00Z", "forecast_value": 100},
                    {"timestamp": "2023-01-01T02:00:00Z", "forecast_value": 105},
                ],
                "prediction_id": "pred_12345",
                "prediction_status": "completed",
                "prediction_timestamp": "2023-01-01T00:00:00Z",
                "request_id": "req_67890",
            }
        }

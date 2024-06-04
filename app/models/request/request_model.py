from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    """Prediction Request Model"""
    request_id: str = Field(..., example="123456")
    ## assuming a Path like: uploads/sample_data/example/sample_dataset.csv
    file_folder: str = Field(..., example="uploads")
    file_path: str = Field(..., example="/sample_data/example")
    file_name: str = Field(..., example="sample_dataset.csv")
    prediction_parameters: dict = Field(..., example={"param1": "value1", "param2": 10})

    class Config:
        schema_extra = {
            "example": {
                "request_id": "123456",
                "file_name": "sample_image.png",
                "file_path": "/uploads/sample_image.png",
                "file_folder": "/uploads",
                "prediction_parameters": {
                    "param1": "value1",
                    "param2": 10
                }
            }
        }

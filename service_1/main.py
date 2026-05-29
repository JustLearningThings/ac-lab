import os
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Service 1 - Public Service")
SERVICE_2_URL = os.getenv("SERVICE_2_URL", "http://localhost:8002")


@app.get("/")
def root():
    return {
        "service": "service-1",
        "message": "Hello from public Service 1"
    }


@app.get("/ask-service-2")
def ask_service_2(name: str = "student"):
    try:
        response = requests.get(
            f"{SERVICE_2_URL}/process",
            params={"name": name},
            timeout=5
        )

        response.raise_for_status()

        data_from_service_2 = response.json()

        return {
            "service": "service-1",
            "message": "Service 1 received your request and contacted Service 2",
            "response_from_service_2": data_from_service_2
        }

    except requests.exceptions.RequestException as error:
        raise HTTPException(
            status_code=500,
            detail=f"Service 1 could not contact Service 2: {str(error)}"
        )
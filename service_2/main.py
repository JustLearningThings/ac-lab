from fastapi import FastAPI

app = FastAPI(title="Service 2 - Internal Service")


@app.get("/")
def root():
    return {
        "service": "service-2",
        "message": "Hello from internal Service 2"
    }


@app.get("/process")
def process_data(name: str = "student"):
    return {
        "service": "service-2",
        "received_name": name,
        "processed_message": f"Service 2 processed data for {name}"
    }
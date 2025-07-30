from fastapi import FastAPI
from .routers import upload

app = FastAPI()
app.include_router(upload.router)

@app.get("/")
async def main():
    return {"message": "Welcome to the Smart File Analyzer API. Use the /upload-file endpoint to upload files for analysis."}
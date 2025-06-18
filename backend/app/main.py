"""To run only backend: cd backend && uvicorn app.main:app --reload --port 8000"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}
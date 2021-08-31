from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""
    
    total = num1 + num2
    return {"total": total}
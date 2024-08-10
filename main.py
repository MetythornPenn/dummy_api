from fastapi import FastAPI, File, UploadFile, Form
import random

app = FastAPI()

@app.post("/register")
async def register(
    image_register: UploadFile = File(...), 
    image_name: str = Form(...)
    ):
    # Here, you would normally process the image and the text string
    # For now, we'll just return a random boolean
    return {"result": random.choice([True, False])}

@app.post("/compare")
async def compare(
    image_register: UploadFile = File(...), 
    image_verify: UploadFile = File(...),
    image_name: str = Form(...)
    ):
    # Here, you would normally process the image and the text string
    # For now, we'll just return a random boolean
    return {"result": random.choice([True, False])}

from fastapi import FastAPI, File, UploadFile
import random 

app = FastAPI()


@app.post("/register")
async def register(
    img1: UploadFile = File(...),
    img2: UploadFile = File(...)
):
    return {
        "result": random.choice([True, False])
    }


@app.post("/compare")
async def compare(
    img1: UploadFile = File(...),
    img2: UploadFile = File(...)
):
    return {
        "result": random.choice([True, False])
    }
    
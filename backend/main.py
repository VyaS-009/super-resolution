from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image
import numpy as np
import os
from model.realesrgan_runner import upscale_image

app = FastAPI()

UPLOAD_FOLDER = "static/inputs"
OUTPUT_FOLDER = "static/outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.post("/enhance")
async def enhance_image(file: UploadFile = File(...)):
    input_path = f"{UPLOAD_FOLDER}/{file.filename}"
    output_path = f"{OUTPUT_FOLDER}/enhanced_{file.filename}"
    
    # Save the uploaded file
    with open(input_path, "wb") as f:
        f.write(await file.read())
    
    # Run inference
    upscale_image(input_path, output_path)
    
    return FileResponse(output_path, media_type="image/png")

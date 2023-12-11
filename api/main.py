import tensorflow as tf
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = load_model("../potatoes_model/1", custom_objects={'SparseCategoricalCrossentropy': SparseCategoricalCrossentropy()})
CLASS_NAME = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "hello, I am alive"

def read_file_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    prediction = MODEL.predict(img_batch)
    prediction_class = CLASS_NAME[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    print(prediction_class,confidence)
    return {
        "class":prediction_class,
        "confidence":float(confidence)
    }

    # Perform any additional processing with the prediction as needed
    # ...

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

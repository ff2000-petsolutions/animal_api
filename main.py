from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from vision_utils import get_products_from_image

app = FastAPI()

# Enable CORS for local testing and DNN frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict this to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_animal(image: UploadFile = File(...)):
    try:
        content = await image.read()
        categories = get_products_from_image(content)
        return {"categories": categories}
    except Exception as e:
        return {"error": str(e)}

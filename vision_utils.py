import os
import io
from google.cloud import vision

# Ensure environment variable for Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "superb-webbing-455211-d7-2e140293e808.json"

# Initialize client
client = vision.ImageAnnotatorClient()

categories = {
    "Dog": "Kutya",
    "Cat": "Macska",
    "Rabbit": "Kisemlősök",
    "Hamster": "Kisemlősök",
    "Guinea pig": "Kisemlősök",
    "Ferret": "Kisemlősök",
    "Mouse": "Kisemlősök",
    "Rat": "Kisemlősök",
    "Gerbil": "Kisemlősök",
    "Fish": "Halak, hüllők",
    "Reptile": "Halak, hüllők",
    "Lizard": "Halak, hüllők",
    "Turtle": "Halak, hüllők",
    "Snake": "Halak, hüllők",
    "Frog": "Halak, hüllők"
}

def detect_animal_from_bytes(image_bytes: bytes):
    image = vision.Image(content=image_bytes)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    detected_labels = [label.description for label in labels]
    matched = list({categories[label] for label in detected_labels if label in categories})

    return matched

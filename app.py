import os
import torch
import numpy as np
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import gradio as gr

# Load model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Function to get image embedding
def get_embedding(image):
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        return model.get_image_features(**inputs)[0].numpy()

# Compare upload to all reference images in /data
def search_database(upload_img):
    threshold = 0.88
    upload_embedding = get_embedding(upload_img)

    for filename in os.listdir("data"):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            ref_img = Image.open(os.path.join("data", filename)).convert("RGB")
            ref_embedding = get_embedding(ref_img)

            similarity = np.dot(upload_embedding, ref_embedding) / (
                np.linalg.norm(upload_embedding) * np.linalg.norm(ref_embedding)
            )

            if similarity > threshold:
                return f"✅ Match found: {filename} (Similarity = {similarity:.2f})"

    return "❌ No similar image found in the database."

# Gradio interface
gr.Interface(
    fn=search_database,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs="text",
    title="🧠 Visual Product Checker",
    description="Upload an image to see if it's already in the store database"
).launch(share=True)


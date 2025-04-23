#  Visual Product Detector with CLIP & Gradio

This project is an AI-powered image comparison tool that allows users to **upload an image** and checks whether a **visually similar product** exists in a predefined image dataset. It leverages OpenAI's [CLIP model](https://github.com/openai/CLIP) for semantic image embedding and [Gradio](https://www.gradio.app) to provide a user-friendly web interface.


---

## 🔍 Features

- ✅ Upload an image and detect if it’s visually similar to items in the store’s dataset
- 🤖 Powered by CLIP for smart image comparison
- 🌐 Web-based UI built with Gradio (no frontend coding needed)
- 🧠 No training required – works out-of-the-box with reference images

---

## Project Structure

   ```bash
visual-product-detector/
├── app.py                  # Main app
├── data/                   # Folder with reference images
│   ├── tomato1.jpg
│   └── onion.jpg

 
```

## 📸 Demo

https://user-example.gradio.live *(use `share=True` in app to generate)*

---

## 🚀 Getting Started


   ```bash
pip install torch torchvision transformers gradio pillow
 
```

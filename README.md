#  Visual Product Detector with CLIP & Gradio

This project is an AI-powered image comparison tool that allows users to **upload an image** and checks whether a **visually similar product** exists in a predefined image dataset. It leverages OpenAI's [CLIP model](https://github.com/openai/CLIP) for semantic image embedding and [Gradio](https://www.gradio.app) to provide a user-friendly web interface.


---

## 🔍 Features

- ✅ Upload an image and detect if it’s visually similar to items in the store’s dataset
- 🤖 Powered by CLIP for smart image comparison
- 🌐 Web-based UI built with Gradio (no frontend coding needed)
- 🧠 No training required – works out-of-the-box with reference images

---
## ✨ Features

- **Image Upload UI** via Gradio
- **Visual Matching** using CLIP’s semantic embeddings
- **Threshold-based detection** to classify “Found” or “Not Found”
- **Extensible dataset**: easily add more product images to the `/data` folder
- **Real-time feedback** in browser – no page reload needed

---

## 🛠 Tech Stack

- Python 3.8+
- [🤗 Transformers](https://huggingface.co/docs/transformers/) (CLIP model)
- [Gradio](https://www.gradio.app/)
- PIL (Pillow) for image processing
- NumPy for similarity calculations

## Project Structure

   ```bash
visual-product-detector/
├── app.py                  # Main app
├── data/                   # Folder with reference images
│   ├── tomato1.jpg
│   └── onion.jpg

 
```

## 📸 Demo

<img width="1159" alt="image" src="https://github.com/user-attachments/assets/7a2086ab-7b7e-48ae-a378-776a89c20417" />


---

## 🚀 Installation requirements


   ```bash
pip install torch torchvision transformers gradio pillow
 
```

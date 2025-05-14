# 🔍 Super Resolution API using Real-ESRGAN

This project implements an **AI-powered image enhancement API** using the Real-ESRGAN model. Designed for upscaling low-resolution images into stunning high-resolution outputs, this solution is perfect for restoring old images, improving clarity, or simply experimenting with generative upscaling.

🏗️ Built with **FastAPI**, it provides a simple yet powerful Swagger UI where users can test the API directly—no frontend needed!

---

## ✨ Features

- ✅ **Real-ESRGAN Integration**: Super-resolve images using the powerful Real-ESRGAN model.
- 🚀 **FastAPI**: Lightning-fast API framework with auto-generated Swagger UI for quick testing.
- 🖼️ **Image Upload & Enhancement**: Upload a low-res image, get a high-res version in return.
- 📁 **Organized Static Folder**: Auto-saves inputs and outputs for easy access and logging.
- 📂 **Modular Structure**: Scalable and clean codebase with reusable model runner.

---

## 🧠 Technology Stack

| Purpose        | Tech             |
| -------------- | ---------------- |
| API Framework  | FastAPI (Python) |
| AI Model       | Real-ESRGAN      |
| Image Handling | PIL, OpenCV      |
| Environment    | Python 3.8+      |

---

## 📁 Project Structure

```
super-resolution-api/
│
├── backend/
│   ├── main.py                          # FastAPI entrypoint
│   ├── model/
│   │   └── realesrgan_runner.py        # Image enhancement logic
│   └── static/
│       ├── inputs/                     # Stores uploaded low-res images
│       └── outputs/                    # Stores enhanced high-res images
│
├── models/
│   └── realesrgan/                     # Place ESRGAN model files here
│
├── requirements.txt
├── folder-structure.txt
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/super-resolution-api.git
cd super-resolution-api
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download ESRGAN Model

Download the pretrained Real-ESRGAN model and place it under:

```
models/realesrgan/
```

> 📌 You can find official weights here:  
> [https://github.com/xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)

### 5. Run the API Server

```bash
cd backend
uvicorn main:app --reload
```

> 🌐 The API will be available at: `http://127.0.0.1:8000`

---

## 🧪 Testing the API via Swagger UI

1. Open your browser and go to:  
   👉 `http://127.0.0.1:8000/docs`

2. Use the `/enhance` endpoint:

   - Click **"Try it out"**
   - Upload a `.jpg` or `.png` image
   - Click **"Execute"**
   - Scroll down to **"Response"** to find the download link for the enhanced image.

3. Enhanced images will be saved to:
   - **Uploaded:** `backend/static/inputs`
   - **Enhanced:** `backend/static/outputs`

---

## 📸 Example Workflow

| Input Image (Low-Res)          | Output Image (Super-Res)         |
| ------------------------------ | -------------------------------- |
| ![Input](./examples/input.jpg) | ![Output](./examples/output.jpg) |

> (Optional: Add example images in an `examples/` folder)

---

## 📌 API Endpoint Reference

### `POST /enhance`

**Description**: Accepts an image file and returns a super-resolved image.

- **Request**: `multipart/form-data`
- **Field Name**: `file`
- **Response**: Path to enhanced image

---

## 🧼 Clean & Extensible Design

- Modular `realesrgan_runner.py` handles all image enhancement logic.
- Static folders (`inputs`, `outputs`) enable reproducibility and logging.
- Easily extend to support frontend, batch processing, or image previews.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 🤝 Acknowledgements

- **[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)** – High-quality image super-resolution models.
- **FastAPI** – Modern web framework for APIs.
- **OpenCV & PIL** – Powerful libraries for image handling and preprocessing.

---

## 💬 Contact

Have feedback, questions, or want to collaborate?

📧 [your.email@example.com](mailto:vedavyas1014@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/vedavyas-viswanatham-3769a2219/) | [GitHub](https://github.com/VyaS-009)

---

> “AI can’t replace creativity, but it can definitely enhance resolution.”

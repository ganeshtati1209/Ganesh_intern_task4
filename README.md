# 🖼️ Pix2Pix: Image-to-Image Translation with Stable Diffusion

This project implements **image-to-image translation** using a **Conditional GAN (cGAN)** called **Pix2Pix**.  
It utilizes **Stable Diffusion** for transforming input images into enhanced versions.

---

## 🚀 Features
- **Performs image-to-image translation** (e.g., sketches → realistic images).
- **Uses Stable Diffusion (`runwayml/stable-diffusion-v1-5`)**.
- **Optimized for MPS (Mac M1/M2), CUDA (Nvidia GPUs), and CPU**.
- **Manually set input image inside `main.py`**.

---

## 📂 Project Structure
```
📁 project-folder
│── 📄 main.py          # Script for image-to-image translation
│── 📄 requirements.txt # Dependencies for the project
│── 📜 README.md        # This file (Instructions & setup guide)
```

---

## 🛠️ Installation & Setup

### ✅ **1. Clone the Repository**
```sh
git clone https://github.com/ganeshtati1209/Ganesh_intern_task4.git
cd YOUR_REPO_NAME
```

### ✅ **2. Create & Activate a Virtual Environment (Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### ✅ **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🎨 Image Translation Instructions

### **1️⃣ Set the Input Image Path**
- Open **`main.py`** and manually set the image file path inside `main()`.
```python
input_image_path = "path/to/your/image.jpg"  # Replace this with your actual image
```

### **2️⃣ Run the Script**
```sh
python main.py
```

### **Example Output**
```
✅ Image translation completed! Saved as 'translated_image.png'
```
- The **output image** will be saved as **`translated_image.png`**.

---

## 🛑 Troubleshooting

### **1️⃣ Out of Memory Issues?**
- Reduce image size inside `main.py`:
```python
strength=0.5  # Lowering strength reduces memory usage
```
- Lower guidance scale:
```python
guidance_scale=5.0
```

### **2️⃣ Running on CPU Instead of MPS?**
- Ensure MPS is enabled in PyTorch:
```python
torch.backends.mps.is_available()
```
- If not available, update PyTorch:
```sh
pip install --upgrade torch torchvision torchaudio
```

---

## 📜 License
This project is open-source under the **MIT License**.

---

## ⭐ Contributing
Feel free to **fork & contribute** by submitting a pull request!

---

## 🔗 References
- [Pix2Pix Paper](https://arxiv.org/abs/1611.07004)
- [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index)
- [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5)

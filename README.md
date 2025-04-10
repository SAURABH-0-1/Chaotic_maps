# 🔒 Image Encryption using XOR and Chaotic Numbers

This project demonstrates how to encrypt a grayscale image using XOR-based encryption with a matrix of chaotic numbers. It uses libraries such as `PIL`, `NumPy`, and `pandas` to manipulate image data and securely generate or reuse random chaotic values.

---

## 📸 Features

- Converts any image to grayscale.
- Generates a matrix of chaotic numbers (or loads if already generated).
- Performs XOR operation for encryption.
- Saves and displays the encrypted image.
- Ensures reproducibility using saved chaotic values.

---

## 🚀 How It Works

1. Load an image and convert it to grayscale.
2. Generate a chaotic matrix (same dimensions as the image) or load an existing one from CSV.
3. Perform a bitwise XOR between the image pixels and chaotic numbers.
4. Save and show the encrypted image.

---

## 🛠️ Installation & Requirements

### 🔗 Libraries Required

Make sure to install the following libraries before running the script:

```bash
pip install pillow numpy pandas
📂 File Structure
📁 project-folder/
│
├── peaky.png                # Input image (grayscale conversion done in code)
├── chaotic_numbers21.csv    # (Auto-generated) Matrix of chaotic numbers
├── Xored-pixeled3.png       # Output encrypted image
└── encrypt.py               # Python script file
📷 Input Image
Make sure to place your image (e.g., peaky.png) in the same folder as the script or update the image_path variable accordingly.

🧪 Run the Script
python encrypt.py

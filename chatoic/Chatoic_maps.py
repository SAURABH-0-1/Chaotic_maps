from PIL import Image
import numpy as np
import pandas as pd
import os

# Image path
image_path = "peaky.png"

# Load the image safely
try:
    img = Image.open(image_path)
except FileNotFoundError:
    print("Error: Image file not found. Ensure the path is correct.")
    exit()

# Convert to grayscale and display---------------------------
img = img.convert('L')  # 'L' mode for grayscale
img_array = np.array(img)  # Convert to NumPy array
img.show()

# Chaotic numbers file
chaotic_numbers_file = "chaotic_numbers21.csv"

# Check if chaotic numbers exist
if not os.path.exists(chaotic_numbers_file):
    np.random.seed(42)  # Set a seed for reproducibility
    chaotic_numbers = np.random.randint(0, 256, img_array.shape, dtype=np.uint8)

    # Save chaotic numbers
    pd.DataFrame(chaotic_numbers).to_csv(chaotic_numbers_file, index=False, header=False)
    print("Chaotic numbers generated and saved.")
else:
    # Load existing chaotic numbers
    chaotic_numbers = pd.read_csv(chaotic_numbers_file, header=None).values.astype(np.uint8)
    print("Loaded existing chaotic numbers.")

# XOR encryption
xor_image = np.bitwise_xor(img_array, chaotic_numbers)

# Save and show encrypted image
encrypted_img = Image.fromarray(xor_image)
encrypted_img.save("Xored-pixeled3.png")
encrypted_img.show()
print("Encrypted image saved.")



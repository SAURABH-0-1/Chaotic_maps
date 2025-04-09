import numpy as np
import pandas as pd
from PIL import Image

# Load the encrypted image (Ensure it's a NumPy array)
xor_image = np.array(Image.open("Xored-pixeled.png"))

# Load the chaotic numbers from CSV
chaotic_numbers_loaded = pd.read_csv("chaotic_numbers21.csv", header=None).values

# Check if the dataset matches the encrypted image's shape
if chaotic_numbers_loaded.shape != xor_image.shape:
    print("Warning: The dataset shape does not match the encrypted image. Ensure you are using the correct chaotic number set.")

# Ensure correct data type and reshape
chaotic_numbers_loaded = chaotic_numbers_loaded.astype(np.uint8).reshape(xor_image.shape)

# XOR decryption (Applying XOR again restores the original image)
decrypted_image = np.bitwise_xor(xor_image, chaotic_numbers_loaded)

# Convert NumPy array to an image and save
decrypted_img = Image.fromarray(decrypted_image)
decrypted_img.save("Decrypted-image2.png")
decrypted_img.show()

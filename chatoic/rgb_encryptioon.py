from PIL import Image
import numpy as np
import pandas as pd

# Load the image and convert it to an RGB NumPy array
image_path = "peaky.png"
img = Image.open(image_path).convert('RGB')  # Keep it RGB
img_array = np.array(img)  # Convert to NumPy array (H, W, 3)

# Generate chaotic random numbers for each channel (R, G, B)
np.random.seed(42)  # Set a seed for reproducibility
h, w, c = img_array.shape  # Get image dimensions
chaotic_numbers = np.random.randint(0, 256, (h, w, c), dtype=np.uint8)  # Generate random values

# Save chaotic numbers
pd.DataFrame(chaotic_numbers.reshape(-1, c)).to_csv("chaotic_numbers_rgb.csv", index=False, header=False)

# XOR operation for encryption
xor_image = np.bitwise_xor(img_array, chaotic_numbers)

# Convert NumPy array back to an image and save
encrypted_img = Image.fromarray(xor_image)
encrypted_img.save("Xored-pixeled-RGB.png")
encrypted_img.show()

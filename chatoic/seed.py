from PIL import Image
import numpy as np
import pandas as pd

# Define key value
key_value = 42  # Isse adjust kar sakte ho for better randomness

# Load the image and convert to grayscale
image_path = "chatoic\python pic.jpg"
img = Image.open(image_path).convert('L')
img_array = np.array(img, dtype=np.uint8)  # Ensure dtype is uint8

# Generate chaotic random numbers using the key
np.random.seed(key_value)  # Fixed seed for reproducibility
chaotic_numbers = np.random.randint(0, 256, img_array.shape, dtype=np.uint8)  # Full grayscale range

# Save chaotic numbers
pd.DataFrame(chaotic_numbers).to_csv("chaotic_numbers.csv", index=False, header=False)

# Encrypt image using XOR
xor_image = np.bitwise_xor(img_array, chaotic_numbers)

# Save and show encrypted image
encrypted_img = Image.fromarray(xor_image)
encrypted_img.save("Xored-pixeled.png")
encrypted_img.show()

# Decrypt image (apply XOR again)
chaotic_numbers_loaded = pd.read_csv("chaotic_numbers.csv", header=None).values.astype(np.uint8)
decrypted_image = np.bitwise_xor(xor_image, chaotic_numbers_loaded)

# Save and show decrypted image
decrypted_img = Image.fromarray(decrypted_image)
decrypted_img.save("Decrypted-image.png")
decrypted_img.show()

import pandas as pd

# Load the CSV file
df = pd.read_csv("random_numbers.csv")

# Drop the Timestamp column
df = df.iloc[:, 1:]  

# Save the cleaned data to a new file
df.to_csv("cleaned_chaotic_numbers.csv", index=False)

print("Timestamp removed. Cleaned data saved as 'cleaned_chaotic_numbers.csv'.")

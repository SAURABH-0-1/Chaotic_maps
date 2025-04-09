import time
import csv
import matplotlib.pyplot as plt
import numpy as np

class ChaoticRNG:
    def __init__(self, seed=0.5, r=3.9):
        self.x = seed
        self.r = r

    def generate_number(self):
        self.x = self.r * self.x * (1 - self.x)  # Logistic Map Equation
        return self.x

# Initialize the chaotic RNG
chaos_rng = ChaoticRNG(seed=0.72, r=3.9)

# New lists to store each pair separately for plotting
history1 = []
history2 = []

# Open a CSV file to store numbers with two columns for the two values
csv_file = "random_numbers.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Chaotic Number 1", "Chaotic Number 2"])

# Set up the plot with two lines for the two series
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
ax.set_title("Chaotic Random Number Generation (Logistic Map)")
ax.set_xlabel("Iteration")
ax.set_ylabel("Random Number")
line1, = ax.plot([], [], "bo-", markersize=5, label="Number 1")
line2, = ax.plot([], [], "ro-", markersize=5, label="Number 2")
ax.legend()

# Generate and update every second
iteration = 0
while True:
    # Generate two chaotic numbers sequentially
    random_number1 = chaos_rng.generate_number()
    random_number2 = chaos_rng.generate_number()
    iteration += 1

    # Append to history lists for plotting
    history1.append(random_number1)
    history2.append(random_number2)

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Get current time
    print(f"{timestamp} - Number 1: {random_number1}, Number 2: {random_number2}")

    # Save to CSV: both numbers in a single row
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, random_number1, random_number2])

    # Update plot for both series
    xs = np.arange(len(history1))
    line1.set_data(xs, history1)
    line2.set_data(xs, history2)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(1)  # Wait for 1 second
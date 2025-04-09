import time
import csv
import matplotlib.pyplot as plt
import numpy as np

class ChaoticRNG:
    def __init__(self, seed=0.5, r=3.9):
        self.x = seed
        self.r = r
        self.history = []  # Store generated values

    def generate_number(self):
        self.x = self.r * self.x * (1 - self.x)  # Logistic Map Equation
        self.history.append(self.x)
        return self.x

# Initialize chaotic RNG
chaos_rng = ChaoticRNG(seed=0.72, r=3.9)

# Open a CSV file to store numbers
csv_file = "random_numbers.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Chaotic Number"])  # Column headers

# Set up the plot
plt.ion()  # Interactive mode ON
fig, ax = plt.subplots()
ax.set_title("Chaotic Random Number Generation (Logistic Map)")
ax.set_xlabel("Time (Seconds)")
ax.set_ylabel("Random Number")
line, = ax.plot([], [], "bo-", markersize=5)  # Blue circles for points

# Generate and update every second
while True:
    random_number = chaos_rng.generate_number()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Get current time
    print(f"{timestamp} - Generated Number: {random_number}")

    # Save to CSV
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, random_number])  # Append new row

    # Update plot
    line.set_xdata(np.arange(len(chaos_rng.history)))  # X-axis: time
    line.set_ydata(chaos_rng.history)  # Y-axis: chaotic values
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(1)  # Wait for 1 second

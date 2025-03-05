import matplotlib.pyplot as plt
import numpy as np

# Given data from the document
N_values = [10, 100, 1000, 10000, 100000]

speedup_values = {
    0.50: [1.818, 1.980, 1.998, 1.9998, 1.99998],
    0.90: [5.263, 9.174, 9.911, 9.991, 9.999],
    0.95: [6.897, 16.806, 19.627, 19.962, 19.996],
    0.99: [9.174, 50.251, 90.992, 99.020, 99.901]
}

# Define colors for different P values
colors = {0.50: 'blue', 0.90: 'red', 0.95: 'green', 0.99: 'purple'}

# Plot the speedup values
plt.figure(figsize=(10, 6))
for P, speedup in speedup_values.items():
    plt.plot(N_values, speedup, marker='o', linestyle='-', color=colors[P], label=f'P = {P * 100:.0f}%')

# Formatting
plt.xscale('log')  # Log scale for x-axis
plt.xticks(N_values, labels=[str(n) for n in N_values])  # Custom x-ticks
plt.xlabel('Number of Processors (N)')
plt.ylabel('Speedup')
plt.title('Speedup vs Number of Processors for Different Parallel Portions')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Show the plot
plt.show()

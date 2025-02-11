import random
import numpy as np

# Define loaded die probabilities
P = {1: 0.12, 2: 0.14, 3: 0.17, 4: 0.20, 5: 0.19, 6: 0.18}
assert abs(sum(P.values()) - 1) < 1e-9, "Probabilities must sum to 1"

# Function to simulate a loaded die roll
def roll_loaded_die():
    x = random.random()
    cumulative = 0.0
    for face, probability in P.items():
        cumulative += probability
        if x < cumulative:
            return face
    return 6  # Fallback to the highest face due to rounding errors

# Step 2: Compute mean and variance
values = np.array(list(P.keys()))
probabilities = np.array(list(P.values()))
mean = np.sum(values * probabilities)
variance = np.sum(probabilities * (values - mean) ** 2)

# Step 3: Simulate Trials and Compute CDF
n = 4000  # Number of rolls per trial
trials = 20000
z_values = np.arange(0, 3.5, 0.01)
cdf_estimates = np.zeros(len(z_values))

for _ in range(trials):
    S_n = sum(roll_loaded_die() for _ in range(n))  # Sum of `n` rolls
    Z_n = (S_n - n * mean) / (np.sqrt(n * variance))  # Normalize using CLT
    cdf_estimates += (Z_n <= z_values).astype(int)


# Normalize CDF estimates
cdf_estimates /= trials

# Step 4: Output Experimental CDF Table
print("Experimental CDF:")
print("         .00     .01     .02     .03     .04     .05     .06     .07     .08     .09")
print("      ------------------------------------------------------------------------------")
for i in range(35):  # 0.0 to 3.4
    row_values = cdf_estimates[i * 10:(i + 1) * 10]
    print(f"{i / 10:.1f} |", "  ".join(f"{val:.4f}" for val in row_values))

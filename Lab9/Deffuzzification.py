import numpy as np

# --- Defuzzification Functions ---

def centroid(x, mf):
    return np.sum(x * mf) / np.sum(mf)

def mean_of_maximum(x, mf):
    max_val = np.max(mf)
    max_indices = np.where(mf == max_val)[0]
    return np.mean(x[max_indices])

# --- Fuzzy Controller ---

def fuzzy_controller(error):
    x = np.linspace(0, 100, 100)  # Output values (0-100%)

    # Fuzzy rules based on error
    if error < -5:
        output_mf = np.maximum(0, 1 - (x / 50))  # Low
    elif -5 <= error <= 5:
        output_mf = np.maximum(0, 1 - abs(x - 50) / 25)  # Medium
    else:
        output_mf = np.maximum(0, (x - 50) / 50)  # High

    # Defuzzification
    center = centroid(x, output_mf)
    mean_max = mean_of_maximum(x, output_mf)

    return center, mean_max

# --- Example Use ---

error = -4  # Try values like -8, 0, or +6

centroid_output, mean_max_output = fuzzy_controller(error)

print("=== Fuzzy Controller Output ===")
print(f"Error: {error}")
print(f"Centroid Defuzzification: {centroid_output:.2f}")
print(f"Mean of Maximum: {mean_max_output:.2f}")

import numpy as np

def func(x):
    return 1 / (1 + x)

# Define the integration bounds and number of subintervals
a = 0
b = 6
n = 6

# Generate the equally spaced points over the interval
x = np.linspace(a, b, n+1)

# Evaluate the function at each of the points
y = func(x)

# Step size
h = (b - a) / n

# Apply Simpson's 1/3 rule
ans = (h / 3) * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))

# Print the result
print(f"Integrated value by Simpson's 1/3 rule is: {ans:.4f}")

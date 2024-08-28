import numpy as np
import matplotlib.pyplot as plt

# Define sequences
x1 = np.array([1, 2, 3, 4])
x2 = np.array([4, 3, 2, 1])

# Calculate DTFT
def dtft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

X1 = dtft(x1)
X2 = dtft(x2)

# Linearity
a = 2
b = 3
X_linear = dtft(a * x1 + b * x2)
plt.figure(figsize=(12, 6))
plt.plot(np.abs(X_linear), label='|a*X1 + b*X2|')
plt.plot(np.abs(a * X1 + b * X2), label='|a*X1| + |b*X2|')
plt.xlabel('Frequency Index')
plt.ylabel('Magnitude')
plt.legend()

# Time-shift
n0 = 1
X_shift = dtft(np.roll(x1, n0))
plt.figure(figsize=(12, 6))
plt.plot(np.abs(X_shift), label='|X1(e^jω)e^(-jωn0)|')
plt.plot(np.abs(X1 * np.exp(-2j * np.pi * n0)), label='|X1(e^jω)|e^(-jωn0)')
plt.xlabel('Frequency Index')
plt.ylabel('Magnitude')
plt.legend()

# Energy Spectral Density
S1 = np.abs(X1) ** 2
S2 = np.abs(X2) ** 2
plt.figure(figsize=(12, 6))
plt.plot(S1, label='S1(ω)')
plt.plot(S2, label='S2(ω)')
plt.xlabel('Frequency Index')
plt.ylabel('Energy Spectral Density')
plt.legend()

# Convolution
x3 = np.convolve(x1, x2, mode='full')
X3 = dtft(x3)
plt.figure(figsize=(12, 6))
plt.plot(np.abs(X3), label='|X1(e^jω) * X2(e^jω)|')
plt.plot(np.abs(X1 * X2), label='|X1(e^jω)| * |X2(e^jω)|')
plt.xlabel('Frequency Index')
plt.ylabel('Magnitude')
plt.legend()

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import cmath


def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            angle = 2 * np.pi * k * n / N
            X[k] += x[n] * (np.cos(angle) - 1j * np.sin(angle))
    return X

# Example usage:
x = [0, 1, 2, 3]
X = dft(x)
print("DFT:", X)	
# Compute magnitude and phase
magnitude = np.abs(X)
phase = np.angle(X)

# Plot magnitude spectrum
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(np.arange(len(magnitude)), magnitude)
plt.title('Magnitude Spectrum (Python DFT)')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

# Plot phase spectrum
plt.subplot(2, 1, 2)
plt.stem(np.arange(len(phase)), phase)
plt.title('Phase Spectrum (Python DFT)')
plt.xlabel('Frequency Bin')
plt.ylabel('Phase (radians)')

plt.tight_layout()
plt.show()	
 
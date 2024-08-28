import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_rate = 1000  # Sampling rate in Hz
duration = 1.0        # Duration in seconds
frequency = 50        # Frequency of the sinusoidal signal in Hz
num_samples = 1000    # Number of samples

# Generate the time vector
t = np.linspace(0, duration, num_samples, endpoint=False)

# Generate the sinusoidal signal
x = np.sin(2 * np.pi * frequency * t)

# Compute the DFT manually
def compute_dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        sum = 0
        for n in range(N):
            angle = 2 * np.pi * k * n / N
            sum += x[n] * (np.cos(angle) - 1j * np.sin(angle))
        X[k] = sum
    return X

X_dft = compute_dft(x)

# Compute the corresponding frequency values
frequencies = np.fft.fftfreq(num_samples, 1/sampling_rate)

# Calculate the magnitude of the DFT
magnitude_dft = np.abs(X_dft)

# Find the index of the peak in the magnitude spectrum
peak_index = np.argmax(magnitude_dft)
peak_frequency = frequencies[peak_index]

# Plot the original signal and its DFT
plt.figure(figsize=(14, 6))

# Plot the original signal
plt.subplot(1, 2, 1)
plt.plot(t, x)
plt.title('Original Sinusoidal Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the magnitude spectrum
plt.subplot(1, 2, 2)
plt.plot(frequencies[:num_samples // 2], magnitude_dft[:num_samples // 2])
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')

plt.show()
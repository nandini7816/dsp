import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
# Load audio file
fs, audio = wavfile.read('np.wav')

# Perform DFT
dft = np.fft.fft(audio)

# Calculate magnitude and phase
magnitude = np.abs(dft)
phase = np.angle(dft)

# Plot magnitude and phase
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.plot(magnitude)
plt.xlabel('Frequency Index')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum')

plt.subplot(122)
plt.plot(phase)
plt.xlabel('Frequency Index')
plt.ylabel('Phase (radians)')
plt.title('Phase Spectrum')

plt.tight_layout()
plt.show()

import numpy as np

# Define parameters
N = 8  # Number of samples
a = 2  # Constant a
b = 3  # Constant b

# Define signals x[n] and y[n]
x = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
y = np.array([8, 7, 6, 5, 4, 3, 2, 1], dtype=float)
#linear combination of x and y
z=a*x+b*y
#perform DTFT on x and y and z
X = np.fft.fft(x)
Y = np.fft.fft(y)
Z = np.fft.fft(z)
#verified linear properity
print("linear property verified:",np.allclose(Z,a*X+b*Y))


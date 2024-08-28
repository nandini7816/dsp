import numpy as np
#define a discrete time signal
n=np.arange(-10,11)
x=np.sin(0.2*np.pi*n)
#compute the DTFT of the signal
X=np.fft.fftshift(np.fft.fft(x))
#apply time shifting property
n0=3
x_shifted=np.roll(x,n0)
X_shifted=np.fft.fftshift(np.fft.fft(x_shifted))
#verify the property
print(np.allclose(X_shifted,np.exp(-1j*0.2*np.pi*n0)*X))

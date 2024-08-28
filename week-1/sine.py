import numpy as np
import matplotlib.pyplot as plt
frequency=200
duration=0.5
sampling_rate=1000
t=np.arrange(0,duration,1/sampling_rate)
signal=np.sin(2*np.pi*frequency*t)
plt.plot(t,signal)
plt.title('200 Hz Sinusoidal Signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
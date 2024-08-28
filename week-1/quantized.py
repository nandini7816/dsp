import numpy as np
import matplotlib.pyplot as plt
frequency=200
duration=0.5
sampling_rate=1000
t=np.arange(0,duration,1/sampling_rate)
signal=np.sin(2*np.pi*frequency*t)
#quantization parameters
l=8
signal_min=min(signal)
signal_max=max(signal)
quantization_step=(signal_max-signal_min)/(l-1)
quantized_signal=np.round((signal-signal_min)/quantization_step)*quantization_step+signal_min
plt.figure(figsize=(10,4))
plt.plot(t,signal,label='Original signal')
plt.step(t,signal,label='Quantized signal')
plt.title('200 Hz Sinusoidal Signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid(True)   
plt.show()
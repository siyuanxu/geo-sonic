import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1.0, 1.0/8000)
x = np.sin(2*np.pi*50*t)[:512] * signal.hann(512, sym=0)

plt.plot(np.hstack([x,x]))
plt.show()

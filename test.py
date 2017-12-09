import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate, t = wavfile.read('cm-01b-440hz.wav') 



sp = np.fft.fft(t)
freqs = np.fft.fftfreq(len(t))*rate

idx = np.argmax(np.abs(sp))
freq = abs(freqs[idx])



plt.plot(abs(freqs),abs(sp))
plt.show()


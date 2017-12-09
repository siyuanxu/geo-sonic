import shutil

# modules for visualizer
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# modules for recorder
import wave, pyaudio
import time # time for time tag

# modules for FFT analysis
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np


########### recorder settings ###########
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 44100
CHANNELS = 1
RECORD_SECONDS = 1
#########################################


def visualizer(sound_file):
    input_data = read(sound_file)
    print(input_data)
    audio = input_data[1]
    plt.plot(audio)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")  
    plt.title("Sample Wav")
    plt.show()

def recorder():
    time_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())+'.wav'
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
    print ('Recording...')
    buffer = []
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        audio_data = stream.read(CHUNK)
        buffer.append(audio_data)
    print ('Record Done')
    stream.stop_stream()
    stream.close()
    pa.terminate()
    wf = wave.open(time_name,'wb') 
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(buffer))
    wf.close()

    # sonic_y = b''.join(buffer)
    # sonic_time = 
    # sonic_x = np.arrange(len(sonic_y))
    # sonic_x = (len(sonic_y)/RATE)
    return time_name


def spectrum_analyzer(wav_file):
    # study from https://github.com/balzer82/FFT-Python/blob/master/FFT-Tutorial.ipynb
    rate, sonic_y = wavfile.read(wav_file) 
    sonic_time = len(sonic_y)/rate
    sonic_x = np.arange(0,sonic_time,sonic_time/len(sonic_y))
    # plt.plot(sonic_x,sonic_y)
    # plt.show()
    slice_range = int(0.05*len(sonic_x))
    t = sonic_x[slice_range:-1*slice_range]
    s = sonic_y[slice_range:-1*slice_range]

    Y = np.fft.fft(s)
    N = int(len(Y)/2+1)

    dt = t[1] - t[0]
    fa = 1.0/dt # scan frequency
    X = np.linspace(0, fa/2, N, endpoint=True)

    # print(max(Y))

    plt.plot(X,np.abs(Y[:N]))
    plt.xlim([10,100])
    plt.show()




this_record = recorder()
# visualizer(this_record)
# spectrum_analyzer('cm-01b-440hz.wav')
spectrum_analyzer(this_record)



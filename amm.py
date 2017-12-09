# modules for recorder
import wave, pyaudio
import time # time for time tag

# modules for FFT analysis
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import seaborn


########### recorder settings ###########
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 44100
CHANNELS = 1
RECORD_SECONDS = 0.5
drop_range = 0.05
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
    slice_range = int(drop_range*len(sonic_x))
    x = sonic_x[slice_range:-1*slice_range]
    y = sonic_y[slice_range:-1*slice_range]

    Y = np.fft.fft(y)
    freqs = np.fft.fftfreq(len(y))*rate

    idx = np.argmax(np.abs(Y))
    peak_freq = abs(freqs[idx])

    figure = plt.figure(figsize=(10,10))

    figure1 = figure.add_subplot(211)
    figure1.plot(x*1000,y)
    figure1.set_xlabel(r'Time ($ms$)')
    figure2 = figure.add_subplot(212)
    figure2.set_xlabel(r'frequency ($Hz$)')
    figure2.plot(abs(freqs),abs(Y))

    figure.suptitle('peak_freq = {}Hz'.format(peak_freq))

    plt.show()

this_record = recorder()
spectrum_analyzer(this_record)



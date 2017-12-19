# This program works in python 3
import os

# modules for signal recorder
import wave
import pyaudio
import time  # time for time tag

# modules for spectrum analysis
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import seaborn


def recorder():
    time_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + '.wav'
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
    print('Recording...')
    buffer = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        audio_data = stream.read(CHUNK)
        buffer.append(audio_data)
    print('Record Done')
    stream.stop_stream()
    stream.close()
    pa.terminate()
    wf = wave.open(time_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(buffer))
    wf.close()
    return time_name


def spectrum_analyzer(wav_file):

    def drop_head_tail(data):
        return data[int(drop_range * len(data)):-1 * int(
            drop_range * len(data))]

    def read_data(wav_file):
        rate, sonic_y = wavfile.read(wav_file)
        sonic_time = len(sonic_y) / rate
        sonic_x = np.arange(0, sonic_time, sonic_time / len(sonic_y))

        if drop_range != 0:
            sonic_x = drop_head_tail(sonic_x)
            sonic_y = drop_head_tail(sonic_y)
        return sonic_x, sonic_y, rate

    def select_signal(sonic_x, sonic_y, noise_gate=noise_gate):
        # use max signal as the start point
        # idx = np.argmax(sonic_y)
        # x = sonic_x[idx:(idx + fft_size)]
        # y = sonic_y[idx:(idx + fft_size)]

        # use noise gate as the start point
        idx = 0
        for i in range(len(sonic_x)):
            if abs(sonic_y[i]) > noise_gate:
                idx = i
                break
        x = sonic_x[idx:(idx + fft_size)]
        y = sonic_y[idx:(idx + fft_size)]
        return x, y

    def fliter(x, y, fliter_range=fliter_range):
        low = fliter_range[0]
        high = fliter_range[1]
        new_x = []
        new_y = []
        for i in range(len(x)):
            if low < x[i] < high:
                new_x.append(x[i])
                new_y.append(y[i])
        return np.array(new_x), np.array(new_y)

    def FFT_process(x, y, rate):
        Y = np.fft.fft(y)
        freqs = np.fft.fftfreq(len(y)) * rate

        fft_x, fft_y = fliter(abs(freqs), abs(Y))
        idx = np.argmax(fft_y)
        peak_freq = fft_x[idx]
        return fft_x, fft_y, peak_freq

    def visualizer(sonic_x, sonic_y, fft_x, fft_y, peak_freq):
        figure = plt.figure(figsize=(6, 6))

        figure1 = figure.add_subplot(311)
        figure1.plot(sonic_x, sonic_y)

        figure2 = figure.add_subplot(312)
        figure2.plot(x * 1000, y)
        figure2.set_xlabel(r'Time ($ms$)')
        figure2.set_ylabel('Amplitude')

        figure3 = figure.add_subplot(313)
        figure3.set_xlabel(r'frequency ($Hz$)')
        figure3.set_ylabel('Amplitude')
        figure3.semilogx(fft_x, fft_y)

        figure.suptitle('peak_freq = {}Hz'.format(peak_freq))

        plt.show()
        return

    sonic_x, sonic_y, rate = read_data(wav_file)
    x, y = select_signal(sonic_x, sonic_y)
    fft_x, fft_y, peak_freq = FFT_process(x, y, rate)
    visualizer(sonic_x, sonic_y, fft_x, fft_y, peak_freq)

    return


########### recorder settings ###########
RATE = 1024
CHANNELS = 1
RECORD_SECONDS = 1.2
fft_time = 100  # ms
noise_gate = 5000  # specific noise gate value
# if 0, the program will calculate
# according to ng_rate
# if not 0, it use the given value
# generally, when testing rock-file materials
# suggest 1000
drop_range = 0.1
fliter_range = [10, 1000]
#####
FORMAT = pyaudio.paInt16
CHUNK = int(RATE / 50)
fft_size = int((fft_time / 1000) * RATE)
#########################################


########### test start ###########
this_record = recorder()
spectrum_analyzer(this_record)
os.system('rm *.wav')

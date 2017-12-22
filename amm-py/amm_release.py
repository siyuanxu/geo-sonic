# This program works in python 3

# modules for signal recorder
import wave
import pyaudio
import time  # time for time tag

# modules for fft analysis
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


class amm(object):
    def __init__(self):
        # super(amm, self).__init__()
        self.RATE = 2048
        self.CHANNELS = 1
        self.RECORD_SECONDS = 2
        self.fft_time = 700
        self.noise_gate = 500
        self.drop_range = 0.1
        self.fliter_range = [10, 1000]
        # do not touch the followings

        self.FORMAT = pyaudio.paInt16
        self.CHUNK = int(self.RATE / 50)
        self.fft_size = int((self.fft_time / 1000) * self.RATE)

    def get_signal(self):
        self.wav_file = time.strftime(
            "%Y-%m-%d_%H-%M-%S", time.localtime()) + '.wav'
        pa = pyaudio.PyAudio()
        stream = pa.open(format=self.FORMAT,
                         channels=self.CHANNELS,
                         rate=self.RATE,
                         input=True,
                         frames_per_buffer=self.CHUNK)
        print('Recording...')
        buffer = []
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            audio_data = stream.read(self.CHUNK)
            buffer.append(audio_data)
        print('Record Done')
        stream.stop_stream()
        stream.close()
        pa.terminate()
        wf = wave.open(self.wav_file, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(pa.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(buffer))
        wf.close()
        return self.wav_file

    def fft_analyzer(self):
        def drop_head_tail(data):
            return data[int(self.drop_range * len(data)):-1 * int(
                self.drop_range * len(data))]

        def read_data(wav_file):
            rate, sonic_y = wavfile.read(wav_file)
            sonic_time = len(sonic_y) / rate
            sonic_x = np.arange(0, sonic_time, sonic_time / len(sonic_y))

            if self.drop_range != 0:
                sonic_x = drop_head_tail(sonic_x)
                sonic_y = drop_head_tail(sonic_y)
            return sonic_x, sonic_y, rate

        def select_signal(sonic_x, sonic_y, noise_gate=self.noise_gate,
                          fft_size=self.fft_size):
            # use noise gate as the start point
            idx = 0
            for i in range(len(sonic_x)):
                if abs(sonic_y[i]) > noise_gate:
                    idx = i
                    break
            x = sonic_x[idx:(idx + fft_size)]
            y = sonic_y[idx:(idx + fft_size)]
            return x, y

        def fliter(x, y, fliter_range=self.fliter_range):
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

        self.sonic_x, self.sonic_y, rate = read_data(self.wav_file)
        self.x, self.y = select_signal(self.sonic_x, self.sonic_y)
        self.fft_x, self.fft_y, self.peak_freq = FFT_process(
            self.x, self.y, rate)

        return self.sonic_x, self.sonic_y,\
            self.x, self.y, self.fft_x, self.fft_y, self.peak_freq

    def visualizer(self):
        figure = plt.figure(figsize=(6, 6))

        figure1 = figure.add_subplot(311)
        figure1.plot(self.sonic_x, self.sonic_y)

        figure2 = figure.add_subplot(312)
        figure2.plot(self.x * 1000, self.y)
        figure2.set_xlabel(r'Time ($ms$)')
        figure2.set_ylabel('Amplitude')

        figure3 = figure.add_subplot(313)
        figure3.set_xlabel(r'frequency ($Hz$)')
        figure3.set_ylabel('Amplitude')
        figure3.semilogx(self.fft_x, self.fft_y)

        figure.suptitle('peak_freq = {}Hz'.format(self.peak_freq))

        plt.show()
        return

    def run_test(self):
        self.get_signal()
        self.fft_analyzer()
        self.visualizer()


if __name__ == '__main__':
    amm_signal = amm()
    amm_signal.run_test()

    import os
    os.system('rm *.wav')

# modules for recorder
import wave
import pyaudio
import time  # time for time tag

# modules for FFT analysis
from scipy.io import wavfile
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
import seaborn


########### recorder settings ###########
CHUNK = 100
FORMAT = pyaudio.paInt16
RATE = 10000
CHANNELS = 1
RECORD_SECONDS = 1
fft_size = 1000
ng_rate = 1000  # noise gate ratiao
noise_gate = 10000  # specific noise gate value
# if 0, the program will calculate
# according to ng_rate
# if not 0, it use the given value
drop_range = 0.01
fliter_range = [10, 1000]
#########################################


def drop_head_tail(data):
    return data[int(drop_range*len(data)):-1*int(drop_range*len(data))]


def recorder():
    time_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())+'.wav'
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
    print('Recording...')
    buffer = []
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
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


def select_signal(sonic_x, sonic_y, noise_gate=noise_gate):
    buffer_size = 100
    test_start = 0

    if noise_gate == 0:
        max_y_list = []
        for i in range(len(sonic_x)):
            buffer_y = sonic_y[i:i+buffer_size]
            max_y = max(abs(buffer_y))
            max_y_list.append(max_y)
        noise_gate = ng_rate*min(max_y_list)

    i = 0

    while test_start == 0:
        buffer_y = sonic_y[i:i+buffer_size]
        if len(buffer_y) < 50:
            break
        max_y = max(abs(buffer_y))
        if max_y > noise_gate:
            test_start = 1
        else:
            i += buffer_size-1

    # print(i,i+fft_size,len(sonic_y))
    if test_start == 0:
        print('no data Recorded, try again')
        plt.plot(sonic_x, sonic_y)
        plt.show()
        plt.title('no efficetive signal')
        return

    x = sonic_x[i:i+fft_size]
    y = sonic_y[i:i+fft_size]
    y = np.hstack([0, y[1:-1], 0])
    return x, y


def fliter(x, y, fliter_range=fliter_range):
    low = fliter_range[0]
    high = fliter_range[1]
    x_new = list(np.hstack([x, low, high]).sort())
    low_index = x_new.index(low)
    high_index = x_new.index(high)
    new_x = x[low_index:high_index]
    new_y = y[low_index:high_index]
    return new_x, new_y


def spectrum_analyzer(wav_file):
    # study from
    # https://github.com/balzer82/FFT-Python/blob/master/FFT-Tutorial.ipynb
    rate, sonic_y = wavfile.read(wav_file)
    sonic_time = len(sonic_y)/rate
    sonic_x = np.arange(0, sonic_time, sonic_time/len(sonic_y))

    sonic_x = drop_head_tail(sonic_x)
    sonic_y = drop_head_tail(sonic_y)

    x, y = select_signal(sonic_x, sonic_y)

    # extend the window
    step = x[-1]-x[0]
    x1 = x
    x2 = x+step
    x3 = x+step+step
    x = np.hstack([x1, x2, x3])
    y = np.hstack([y, y, y])

    Y = np.fft.fft(y)
    freqs = np.fft.fftfreq(len(y))*rate

    # freqs, Y = fliter(freqs, Y)

    idx = np.argmax(np.abs(Y))
    peak_freq = abs(freqs[idx])

    print('peak_freq is ', peak_freq+0.5, 'Hz')

    figure = plt.figure(figsize=(6, 6))

    figure1 = figure.add_subplot(311)
    figure1.plot(sonic_x, sonic_y)

    figure2 = figure.add_subplot(312)
    figure2.plot(x*1000, y)
    figure2.set_xlabel(r'Time ($ms$)')
    figure2.set_ylabel('Amplitude')

    figure3 = figure.add_subplot(313)
    figure3.set_xlabel(r'frequency ($Hz$)')
    figure3.set_ylabel('Amplitude')
    figure3.semilogx(abs(freqs), abs(Y))
    # figure2.set_xlim(0,1000)

    figure.suptitle('peak_freq = {}Hz'.format(peak_freq+0.5))

    plt.show()


# init()
this_record = recorder()
spectrum_analyzer(this_record)
# spectrum_analyzer('demo2.wav')
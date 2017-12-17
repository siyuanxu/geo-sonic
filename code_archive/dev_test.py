import os
from amm_pack_dev import *

# ########### recorder settings ###########
# RATE = 44100
# CHANNELS = 1
# RECORD_SECONDS = 2
# fft_time = 500  # ms
# ng_rate = 0  # noise gate ratiao
# noise_gate = 10  # specific noise gate value
# # if 0, the program will calculate
# # according to ng_rate
# # if not 0, it use the given value
# drop_range = 0.01
# fliter_range = [10, 10000]
# #####
# FORMAT = pyaudio.paInt16
# CHUNK = int(RATE / 50)
# fft_size = int((fft_time / 1000) * RATE)
# #########################################


def unit_test():
    i = 0
    results = []
    while i < 10:
        this_record = recorder()
        peak_freq = spectrum_analyzer(this_record)
        results.append(peak_freq)
        os.remove(this_record)

        i += 1
    # results_fig = plt.figure()
    # fig = results_fig.add_subplot(111)
    print(results)


def regular_test():
    this_record = recorder()
    spectrum_analyzer(this_record)


if __name__ == '__main__':
    regular_test()
    os.system('rm *.wav')

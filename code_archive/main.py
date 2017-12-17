import os
from amm_pack_release import *

########### recorder settings ###########
RATE = 5000
CHANNELS = 1
RECORD_SECONDS = 2
fft_time = 500  # ms
ng_rate = 0  # noise gate ratiao
noise_gate = 10  # specific noise gate value
# if 0, the program will calculate
# according to ng_rate
# if not 0, it use the given value
drop_range = 0.01
fliter_range = [10, 1000]
#####
FORMAT = pyaudio.paInt16
CHUNK = int(RATE/50)
fft_size = int((fft_time/1000)*RATE)
#########################################


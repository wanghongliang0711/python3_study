"""
@author: wanghongliang
@file: demo03.py
@time: 2022/3/23 14:27 
"""
import time
import wave
import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt


wave_path = r"D:\work\temp\voice_handle\voice_handle_R01\voice\20220324_102606.wav"


file = wave.open(wave_path)
# print('---------声音信息------------')
# for item in enumerate(WAVE.getparams()):
#     print(item)
a = file.getparams().nframes  # 帧总数
f = file.getparams().framerate  # 采样频率
print(a)
print(f)
sample_time = 1 / f  # 采样点的时间间隔
time1 = a / f  # 声音信号的长度
sample_frequency, audio_sequence = wavfile.read(wave_path)
# print(audio_sequence)  # 声音信号每一帧的“大小”
x_seq = np.arange(0, time1, sample_time)
print(x_seq)
np.savetxt('out.txt', audio_sequence, delimiter=",", fmt="%.3f,%.3f")
# for i in audio_sequence:
#     if i[0] > 500 or i[1] > 500:
#         print(i)
    # if i[0] < -500 or i[1] < -500:
    #     print(i)

for index, item in enumerate(audio_sequence):
    # print(index, item)
    if abs(item[0]) > 500 or abs(item[1]) > 500:
        print(index)
        break



# print(len(x_seq))
# print(len(audio_sequence))
# print(x_seq[0:10])
# print(audio_sequence[0:10])
plt.plot(x_seq, audio_sequence)
plt.xlabel("time (s)")
plt.show()



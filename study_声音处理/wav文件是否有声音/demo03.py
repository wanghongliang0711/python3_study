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


wave_path = r"D:\Study\python\python3_study\python3_study\study_声音处理\录音\test.wav"


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
# np.savetxt('out.txt', audio_sequence, delimiter=",", fmt="%.3f,%.3f")
for i in audio_sequence:
    if i[0] > 500 or i[1] > 500:
        print(i)

# for index, item in enumerate(audio_sequence):
#     print(index, item)
#     time.sleep(100)



print(len(x_seq))
print(len(audio_sequence))

plt.plot(x_seq, audio_sequence, 'blue')
plt.xlabel("time (s)")
plt.show()



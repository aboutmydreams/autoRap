import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import wave

file = wave.open('./try_test/me2.wav')

a = file.getparams().nframes  # 帧总数
print("帧总数,总共采样的次数", a)

f = file.getparams().framerate  # 采样频率
print("采样频率,每秒采集多少次", f)

sample_time = 1 / f  # 采样点的时间间隔
time = a / f  # 声音信号的长度
print("声音信号的长度", time)

sample_frequency, audio_sequence = wavfile.read('./try_test/me2.wav')
# 声音信号每一帧的“大小” https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.io.wavfile.read.html
print(audio_sequence)

x_seq = np.arange(0, time, sample_time)
print(x_seq)

plt.plot(x_seq[::10000], audio_sequence[::10000], 'blue')
plt.xlabel("time (s)")
plt.show()

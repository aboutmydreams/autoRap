# 语音信号卷积
"""
Created on Tue Mar  5 17:40:20 2019
@author: whypan
"""
import wave
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager as font
my_font = font.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")


def waveread(filename):
    f = wave.open(filename, "rb")
    params = f.getparams()
    print(params)
    nchannels, samplewidth, framerate, nframes = params[:4]
    str_data = f.readframes(nframes)
    f.close()
    wave_data = np.frombuffer(str_data, dtype=np.int16)
    wave_data.shape = -1, nchannels
#    wave_data = wave_data.T
    return nchannels, samplewidth, framerate, nframes, wave_data


if __name__ == "__main__":
    print("start")
    channel, samplewidth, framerate, nframes, wave_data = waveread(
        "./try_test/me2.wav")
    s = np.arange(1, nframes+1)
    t = s/framerate
    x = wave_data / np.max(abs(wave_data))
    y = np.transpose(np.random.randn(1, nframes))
    y = y / np.max(abs(y))
    z = y+x
    z = z/np.max(abs(z))

    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(t, x)
    plt.xlabel("time/s")
    plt.ylabel("归一化幅值", fontproperties=my_font)
    plt.title("原始信号", fontproperties=my_font)

    plt.subplot(3, 1, 2)
    plt.plot(t, y)
    plt.xlabel("time/s")
    plt.ylabel("归一化幅值", fontproperties=my_font)
    plt.title("随机序列", fontproperties=my_font)

    plt.subplot(3, 1, 3)
    plt.plot(t, z)
    plt.xlabel("time/s", fontproperties=my_font)
    plt.ylabel("归一化幅值", fontproperties=my_font)
    plt.title("叠加信号", fontproperties=my_font)
    plt.show()

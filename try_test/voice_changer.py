import librosa
y, sr = librosa.load("try_test/me2.wav")
# 通过改变采样率来改变音速，相当于播放速度X2
librosa.output.write_wav("gg_resample.wav", y, sr*2)

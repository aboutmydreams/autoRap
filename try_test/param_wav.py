import wave
win= wave.open('try_test/me2.wav', 'rb')
# wout= wave.open('try_test/me.wav', 'wb')

t0, t1= 1.0, 2.0 # cut audio between one and two seconds
s0, s1= int(t0*win.getframerate()), int(t1*win.getframerate())
# print(win.readframes(s0)) # discard
print(win.getframerate()) # discard
frames = win.readframes(s1-s0)
# print(frames)
# wout.setparams(win.getparams())
# wout.writeframes(frames)

win.close()
# wout.close()
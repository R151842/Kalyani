import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
fs,data=wav.read('myvoice.wav')
fs1,data1=wav.write('high_myvoice.wav',2*fs,data1)
t=np.arange(0,len(data)/fs,1.0/fs)
t1=np.arange(0,len(data1)/fs,1.0/fs1)
print(fs1,data1)
print(fs,data)
plt.subplot(211)
plt.plot(t,data)
plt.subplot(212)
plt.plot(t1,data1)
plt.show()
#t=np.arange(0,len(data)/fs,1.0/fs)
#print(fs,len(data))
#plt.plot(t,data)
#plt.show()

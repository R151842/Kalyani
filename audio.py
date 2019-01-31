import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
fs,data=wav.read('myvoice.wav')
plt.plot(fs,data)
plt.show()
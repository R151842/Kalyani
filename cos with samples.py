import matplotlib.pyplot as plt
import numpy as np
fs=1000
f=5
sample=1000
x=np.arange(sample)
y=np.cos(2*np.pi*f*x/fs)
plt.plot(x,y)
plt.xlabel('voltage')
plt.ylabel('sample')
plt.show()
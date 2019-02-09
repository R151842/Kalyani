import matplotlib.pyplot as plt
import numpy as np
#import scipy.io.wavefile as wav
p=input('enter order=')
f=20
fs=100
y=np.arange(fs)
x=np.sin(2*np.pi*f*y/fs)
f1=200
fs1=100
z=np.arange(fs1)
N=np.sin(2*np.pi*f1*z/fs)
xN=x+N
q=[]
for i in range(0,xN.shape[0]):
	q=np.append(y,np.sum(xN[i:i+p]/p))
plt.subplot(411)
plt.plot(x)
plt.subplot(412)
plt.plot(N)
plt.subplot(413)
plt.plot(xN)
plt.subplot(414)
plt.plot(q)
plt.show()

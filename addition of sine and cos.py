import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,10,1)
x1=np.sin(5*np.pi*t)
print x1
plt.subplot(1,3,1)
plt.stem(t,x1)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('sine')
x2=np.cos(5*np.pi*t)
print x2
plt.subplot(1,3,2)
plt.stem(t,x2)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('cosine')
x=x1+x2
print x
plt.subplot(1,3,3)
plt.stem(t,x)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('addition of cos and sine')
plt.show()

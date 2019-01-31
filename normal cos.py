import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,10,0.1)
x1=np.cos(2*np.pi*t)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(t,x1)
plt.show()
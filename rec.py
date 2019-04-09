import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
wr=[]
m=input("enter no.of samples:")
for n in range(0,m):
	wr=np.append(wr,1)
plt.subplot(231)
plt.title('rectangular')
plt.stem(wr)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=input('enter seq1')
h=input('enter seq2=')
lx=len(x)
lh=len(h)
y=[]
for n in range(lx+lh-1):
	s=0
	for k in range(lx):
		if (n-k<lh and n-k>=0):
			s=s+x[k]*h[n-k]
	y=np.append(y,s)
print(y)

y1=np.convolve(x,h)
print(y1)
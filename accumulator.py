import matplotlib.pyplot as plt
import numpy as np
n=10
sum=0
for i in range(1,n):
	sum=sum+i
	print sum
	plt.plot(i,sum)
plt.show()
	
	
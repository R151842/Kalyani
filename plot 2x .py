import matplotlib.pyplot as plt
n=10
for i in range(0,n,1):
	x=2*i
plt.plot(i,x)
plt.axis([0, n+10, 0, n+10])
plt.show() 
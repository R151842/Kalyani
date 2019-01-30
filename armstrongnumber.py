num=input('enter a number=')
s=0
n=num
while(num!=0):
	m=num%10
	s=s+(m**3)
	num=num/10
if(s==n):
	print('armstrong number')
else:
	print('not armstrong number')
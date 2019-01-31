num=input('enter a number=')
sum=0
while(num!=0):
	t=num%10
	sum=sum+t
	num=num/10
print('sum of the digits=',sum)
	
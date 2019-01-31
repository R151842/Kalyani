def sum(a,b):
	a=a+b
	return a
def sub(a,b):
	if(a>b):
		a=a-b
		return a
	else:
		b=b-a
		return b
def mul(a,b):
	a=a*b
	return a
def div(a,b):
	a=a/b
	return a
def sqr(a):
	x=math.sqrt(a)
	return x



while(True):
	print('choose any operation ')
	print('\n\t1.addition')
	print('\n\t2.subtraction')
	print('\n\t3.multiplication')
	print('\n\t4.divison')
	print('\n\t5.square root')
	print('\n\t6.exit')
	
	choice=input('enter your choice')
	if choice==1:
		print('enter any two numbers')
		num1=input('enter num1 value')
		num2=input('enter num2 value')
		s=sum(num1,num2)
		print('sum=%s'%s)
	elif choice==2:
		print('enter any two numbers')
		num1=input('enter num1 value')
		num2=input('enter num2 value')
		st=sub(num1,num2)
		print('sub=%s'%st)
	elif choice==3:
		print('enter any two numbers')
		num1=input('enter num1 value')
		num2=input('enter num2 value')
		m=mul(num1,num2)
		print('product=%s'%m)
	elif choice==4:
		print('enter any two numbers')
		num1=input('enter num1 value')
		num2=input('enter num2 value')
		d=div(num1,num2)
		print('sum=%s'%d)
	elif choice==5:
		print('enter any  numbers')
		num=input('enter number')
		sq=sqr(num)
		print('square root=%s' %sq)
	else:
		print('byeeeeeeeee')
		break
		
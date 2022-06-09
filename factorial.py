def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factorial(n-1)
num=int(input("Enter the number: "))
if num<0:
	print("Sorry factorial doesn't exists")
else:
	result=factorial(num)
	print("factorial of {0} is {1}".format(num,result))

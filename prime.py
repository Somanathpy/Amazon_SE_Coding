'''     How would you write a function to check if a number is   prime? What kind of tests would you write for this function? '''
num = int(input("enter a number:"))
def is_prime(num):
	#num = abs(num)
	x = True
	if num <= 1:
		x= False
	else:	
		for i in range(2,num):
			if num % i == 0:
				x = False
				break
	if x:
		print(str(num)+" is a Prime Number")
	else:
		print(str(num)+" is Not a Prime Number ")
			
is_prime(num)
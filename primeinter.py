'''Print prime number between interval and how many prime numbers'''
def prime_interval():
	lower = int(input("Enter lower range:"))
	upper = int(input("Enter upper range:"))
	count = 0
	print("Prime numbers between "+str(lower)+" and "+str(upper)+" are")
	for num in range(lower,upper+1):
		if num >1:
			for i in range(2,num):
				if num % i == 0:
					break
			else:
				print(num)
				count += 1
	print("there are "+str(count)+" prime numbers")
prime_interval()
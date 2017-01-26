'''check to see if a given string is a palindrome or not'''
def is_palindrome(str):
	l = len(str)
	list_s = list(str)
	for i in  range(0,l):
		if list_s[i] != list_s[l-i-1]:
			return False
	return True
str = input("enter a string:")
if is_palindrome(str):
	print(str +" is a Palindrome")
else:
	print(str+" is not a palindrome")
	
	
'''
str = input("enter a string:")
if str == str[::-1]:
	print("Palindrome")
else:
	print("not a palindrome")'''
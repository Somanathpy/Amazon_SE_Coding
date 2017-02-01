#without a function
'''
str = input("enter a word:")
str = list(str)
l = len(str)
tester = None
for i in range(0,l):
	if str[i] != str[l-i-1]:
		tester = False
	else:
		tester = True
if tester:
	print("Palindrome")
else:
	print("Not a palindrome")'''
	
#with a function
def is_palindrome(word):
	#word = input("enter a word")
	word = list(word)
	l = len(word)
	for i in range(0,l):
		if word[i] != word[l-i-1]:
			return False
	return True
word = input("enter a string: ")	
if is_palindrome(word):
	print(word+"  is a Palindrome ")
else:
	print(word+"  is not a palindrome")
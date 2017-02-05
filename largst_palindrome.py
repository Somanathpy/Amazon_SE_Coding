# Finding the Longest Palindrome Sub-String in the given string.

'''finding the longest substring which is a palindrome in a given string.
ex: forgeeksskeeg, in this string largest palindrome is -> geeksskeeg, and index is 3 the blow code perform that''' 

def palindromes(string):
	string = string.lower()
	results = []
	for i in range(len(string)):
		for j in range(0,i):
			chunk = string[j:i+1]
			if chunk == chunk[::-1]:
				results.append(chunk)
	return max(results,key=len),string.index(max(results,key=len))
string = input("enter a string:")
print(palindromes(string))
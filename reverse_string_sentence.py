str = input("enter a string:")
str = str.split()

result = []
def word_reverse(word):
	word = list(word)
	l = len(word)
	reverse_word = []
	for i in range(0,l):
		reverse_word.append(word[l-i-1])
	return "".join(reverse_word)
for word in str:
	#word = word[::-1]
	word = word_reverse(word)
	result.insert(0,word)
	
print((" ").join(result))
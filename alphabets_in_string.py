# From the given string, print the Alphabets which occur more than once in the string.

text = input("enter a string:")
di = {}

for i in range(len(text)):
	if text[i].isalpha():
		if text[i] in di:
			di[text[i]] += 1
		else:
			di[text[i]] = 1
for k,v in di.items():
	if v >1:
		print(k,v)

output:
enter a string:abccaa
a 3
c 2
string = input("enter any string:")

string = string.replace(" ","")
#print(string)

chars = {}

for i in range(len(string)):
	if string[i] in chars:
		chars[string[i]] += 1
	else:
		chars[string[i]] = 1
most = 0
most_key = None

for k,v in chars.items():
	if v > most:
		most = v
		most_key = k
print(most_key,most)
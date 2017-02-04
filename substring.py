def isSubString(string1,string2,m,n): 
	#basecases
	if m == 0: return True
	if n == 0: return False
	
	#if last characters of the strings matched!
	if string1[m-1] == string2[n-1]:
		return isSubString(string1,string2,m-1,n-1)
	#if last characters of the strings don't match below line of code works
	return isSubString(string1,string2,m,n-1)


string1 = input("enter a string:")
string2 = input("enter a string:")

#small word should be saved in string1, below if condition will do it.
if len(string2) < len(string1):
	string2,string1 = string1,string2
	
m = len(string1) # length of String1
n = len(string2) #length of string2
#print("string1:"+string1)
#print("string2:"+string2)
if isSubString(string1,string2,m,n):
	print("YES!!!"+string1+" is a substring of "+string2)
else:
	print("NO!!!"+string1+" is not a substring of "+string2)
def isSubSequence(str1,str2,m,n):
	if m == 0: return True
	if n == 0: return False
	if str1[m-1] == str2[n-1]:
		return isSubSequence(str1,str2,m-1,n-1)
	else:
		return isSubSequence(str1,str2,m,n-1)

str1 = input("enter str1:")
str2 = input("enter str2:")
m = len(str1)
n = len(str2)
if isSubSequence(str1,str2,m,n):
	print("yes")
else:
	print("No")
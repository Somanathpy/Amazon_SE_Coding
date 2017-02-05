#source =>http://www.programmingmonk.com/how-to-list-files-in-a-directory-in-python/

# list Path,Directory names, and files in given path
from os import walk
f = []
path ="C:\\Users\\SomandLily\\Desktop\\Python"
for (dirpath, dirnames, filenames) in walk(path):
	path = dirpath
	directories = dirnames
	files = filenames
	break
print("========PATH==========================")
print(path)
print("==================================")
print("///////////////////////////////////")
print("===========DIRECTORIES==============")

for i in directories:
	print(i)
print("==================================")
print("///////////////////////////////////")

print("=============FILES=====================")
for i in files:
	print(i)
print("///////////////////////////////////")


#writes all the files from directiories and sub directories into a new text file
import os
a = open("C:\\Users\\SomandLily\\Desktop\\Python\\output.txt","w")
for path,subdirs,files in os.walk(r'C:\Users\SomandLily\Desktop\Python'):
	for filename in files:
		f = os.path.join(path,filename)
		a.write(str(f)+os.linesep)

		
#print only text files from given path including folders and subfolders
import os,glob
dirlist = glob.glob("C:\\Users\\SomandLily\\Desktop\\Python\\*.txt")
for f in dirlist:
	print(f)


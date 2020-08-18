import os
a = 'blabla'
#get current working dir = os.getcwd()
b = os.getcwd()
print("cwd is:", b)
#change working dir to C:\temp - use DOUBLE \\ !!   os.chdir("path with \\")
os.chdir("C:\\temp")

b = os.getcwd()
print("cwd is:", b)
#list files in currend directory
print("files in this dir: ", os.listdir())

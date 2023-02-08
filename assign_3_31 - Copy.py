#31.	Write a Python program to remove existing indentation from all of the lines in a given text 

def remove_indentation(s):
    for i in s:
        print(i.replace('\t',''))


str_31 = open('kiran.txt','r+')
s = str_31.readlines()
print(s)
str_31.close()
remove_indentation(s)
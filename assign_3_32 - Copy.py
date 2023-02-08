#32.	Write a Python program to add prefix text to all of the lines in a string.  


def prefix(str_32,str_32_prefix):
    for i in str_32:
        print(str_32_prefix+i)

str_32 = input("Enter a lines : ").split('\\n')
str_32_prefix = input("Enter a prefix : ")
print(str_32)
prefix(str_32,str_32_prefix)
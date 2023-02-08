#33.	Write a Python program to set the indentation of the first line.  

def set_indentation(str_33):
    print('\t'+str_33[0])
    for i in str_33[1:]:
        print(i)

str_33 = input("Enter a paragraph : ").split('\\n')
set_indentation(str_33)
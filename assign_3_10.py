#10.	Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'

str_10 = input("Enter any string : ")
if str_10[-3:]=='ing' and len(str_10)>=3:
    print(str_10+'ly')
elif str_10[-3:]!='ing' and len(str_10)>=3:
    print(str_10+'ing')
else:
    print(str_10)
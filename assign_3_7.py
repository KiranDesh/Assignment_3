#7.	Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String

str_1_2 = input("Enter a string you will get string made up of 1st and last 2 character of your typed string: ")
str_made = str_1_2[:2]+str_1_2[-2:]
if len(str_made)==4:
    print(str_made)
else:
    print("Empty String")
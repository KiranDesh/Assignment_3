#9.	Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

str_9 = input('Enter string one : ').split(',')
str1 = str_9[0]
print(type(str1))
str2 = str_9[1]
t = str1.replace(str1[:2],str2[:2])
s = str2.replace(str2[:2],str1[:2])
print(t,",",s)
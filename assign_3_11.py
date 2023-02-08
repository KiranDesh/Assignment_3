#11.	Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'

str_11 = input("Enter any string : ")
sub_s1 = str_11.index("not")
sub_s2 = str_11.index('poor')
new_str= str_11[sub_s1:sub_s2+4]
if ('not' and 'poor' in str_11):
    print(str_11.replace(new_str,'good'))
else:
    print(str_11)
#8.	Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'

sample_str = input("Enter a string and we will replace second occurence of 1st character by '$' :")
sample_str1 = sample_str[1:]
for i in sample_str1:
    if sample_str[0]==i:
        s = sample_str1.replace(i,'$')
        print(sample_str[0]+s)
#6.	Write a Python program to count the number of characters (character frequency) in a string
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

str_chr_count = [i for i in (input("Enter a string you want to count its character : "))]
print({i:str_chr_count.count(i) for i in str_chr_count})
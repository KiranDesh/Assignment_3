#12.	Write a Python function that takes a list of words and return the longest word and the length of the longest one. 
#Sample Output:
#Longest word: Exercises
#Length of the longest word: 9

def longest_word(str_12):
    for i in str_12:
        if len(i) == max([len(i) for i in str_12]):
            print('Longest word: ',i)
            print('Length of the longest word: ',max([len(i) for i in str_12]))
str_12 = input("Enter strings with space :").split(" ")
longest_word(str_12)
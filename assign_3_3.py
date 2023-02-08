#3.	Write a program to accept 10 different strings and convert it into dictionary and print it.
list2 = [input("Enter any 10 string and we will convert it into dictionary "+str(i)+' : ') for i in range(1,11)]
print()
print("HERE YOU CAN CHECK YOUR CREATED DICTIONARY -----",{i:list2.index(i) for i in list2},sep='\n')
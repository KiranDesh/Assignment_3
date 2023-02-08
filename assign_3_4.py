#4.	Write a program to accept 10 different strings and convert it into tuple and print it.
list3 = [input("Enter any 10 string and we will convert it into tuple "+str(i)+" : ") for i in range(1,11)]
print()
print("HERE YOU CAN CHECK YOUR CREATED TUPLE -----",tuple(list3),sep='\n')
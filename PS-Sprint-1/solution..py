# Write a program to generate multiplication tables for a given number.

def generateMultiplicationTable(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)
        
number = int(input("number = "))
generateMultiplicationTable(number)
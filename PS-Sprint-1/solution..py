# Write a program to determine the length of a string without using built-in functions.

def lengthOfString(string):
    count = 0
    for _ in string:
        count += 1
    return count

string = input("string = ")
result = lengthOfString(string)
print(result)
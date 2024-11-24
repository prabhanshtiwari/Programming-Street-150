# Write a program to reverse a given string.  


def reverseString(string):
    reverse_string = ""
    for i in string:
        reverse_string = i + reverse_string
    return reverse_string

string = "aprogramming"
result = reverseString(string)
print(result)

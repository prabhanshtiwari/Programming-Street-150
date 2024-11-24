# Write a program to check if a string or number is a palindrome.

def checkPalindrome(str):
    if (str == str[::-1]):
        return "Palindrome"
    else:
        return "Not Palindrome"

str = input("string/number = ")
result = checkPalindrome(str)
print(result)
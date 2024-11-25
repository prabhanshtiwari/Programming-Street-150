#  Write a program to determine if a number is a perfect number.

def checkPerfectNumber(number):
    
    if (number <= 1):
        return "No perfect numbers below 2"
    
    sum = 0
    for i in range(1, number):
        if (number % i == 0):
            sum = sum + i
    if (sum == number):
        return "Perfect Number"
    else:
        return "Not Perfect Number"

number = int(input("number = "))
result = checkPerfectNumber(number)
print(result)
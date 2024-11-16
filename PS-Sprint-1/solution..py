# Write a program to determine if a number is prime.  
"""
    Input: `number = 7`  
    Output: `Prime`  
    Explanation: 7 has no divisors other than 1 and itself, so it is a prime number.
"""

def checkPrime(number):
    count = 0
    for i in range(1, (int(number ** 0.5))+ 1):
        if (number % i == 0):
            count = count + 1
            if (number/i != i): # other divisor
                count = count + 1
        if (count > 2):
            break        
    if (count == 2):
        return "Prime"
    else: 
        return "Not Prime"
    

number = int(input("number = "))
result = checkPrime(number)
print(result)

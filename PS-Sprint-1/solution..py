def sumDigits(number):
    sum = 0
    while (number != 0):
        remainder = number % 10     # finding the last digits
        sum = sum + remainder       # adding the last digit in sum
        number //= 10               # Dropping the last digit of the number
    return sum
    
number = int(input("number = "))
print(sumDigits(number))


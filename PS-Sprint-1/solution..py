def sumOFSqauresOfDigits(number):
    total_sum = 0
    if number == 0:
        return 0
    while number > 0:
        digit = number % 10;
        total_sum = total_sum + (digit ** 2)
        number = number // 10
    return total_sum

number = int(input("number = "))
result = sumOFSqauresOfDigits(number)
print(result)
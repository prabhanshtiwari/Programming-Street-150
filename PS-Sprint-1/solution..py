def checkPerfectSquare(number):
    sqrt = int(number ** 0.5)
    if (sqrt * sqrt) == number:
        return True
    else:
        return False

number = int(input("number = "))
result = checkPerfectSquare(number)
print(result)
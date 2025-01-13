
def checkArmstrong(num):
        temp = num
        sum = 0
        while (num > 0):
            lastDigit = num % 10
            sum = sum + (lastDigit ** 3)
            num = num // 10
        if (temp == sum):
            return True
        else:
            return False
        
def armstrongNumberInRange(num_range):
    start = num_range[0]
    end = num_range[1]
    numList = []
    for i in range(start, end + 1):
        if (checkArmstrong(i)):
            numList.append(i)
    return numList

num_range = [1, 500]
result = armstrongNumberInRange(num_range)
print(result)
def sumOfElements(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

array = [1, 2, 3, 4, 5]
result = sumOfElements(array)
print(result)
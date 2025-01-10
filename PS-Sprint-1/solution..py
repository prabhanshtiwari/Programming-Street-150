def avfOfArray(array):
    total_sum = 0
    avg = 0
    for i in range(len(array)):
        total_sum += array[i]
    avg = total_sum / len(array)
    return avg

array = [1, 2, 3, 4, 5, 6]
result = avfOfArray(array)
print(result)
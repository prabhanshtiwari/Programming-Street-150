# Write a program to find the largest and smallest numbers in an array.

def checkLargestAndSmallest(array):
    largest = smallest = array[0]
    for i in range(0, len(array) - 1):
        if array[i] > largest:
            largest = array[i]
        if array[i] < smallest:
            smallest = array[i]
    return largest, smallest

array = [4, 7, 1, 8, 5]
result = checkLargestAndSmallest(array)
print("Lasgest:", result[0], "Smallest:", result[1])
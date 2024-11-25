# Write a program to find the second largest number in an array.

def findSecondLargestNumber(array):
    if (len(array) < 2):
        return "Array must contain atleast two elements"
    sorted_array = sorted(set(array))    # sort in ascending order
    secondLargstNumber = sorted_array[-2]
    return secondLargstNumber

array = [11]
result = findSecondLargestNumber(array)
print(result)
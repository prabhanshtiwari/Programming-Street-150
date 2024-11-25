# Write a program to generate a pyramid of numbers (e.g., 1, 12, 123, etc.).


    
def pyramidOfNumbers(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end = "")
        print()
        
rows = int(input("rows = "))
pyramidOfNumbers(rows)
# Write a program to generate the Fibonacci series up to a given number.

def fibonacciSeries(number):
    f0 = 0
    f1 = 1
    fn = f0 + f1

    while (fn < number):
        print(fn, end = " ")
        f0 = f1
        f1 = fn
        fn = f0 + f1

number = int(input("Enter the limit in numeric format: "))
print("Fibonacci Series")
fibonacciSeries(number)
    

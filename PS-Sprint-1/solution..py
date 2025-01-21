def generatingTable(start, end):
    for i in range(1, 11):
        num = start
        while (num <= end):
            print(num, "x", i, "=", num * i, end = "\t" )
            num += 1
        print()

start = 2
end = 4
generatingTable(start, end)
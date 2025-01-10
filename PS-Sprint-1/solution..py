def powerOfNumber(base, exponent):
    result = base ** exponent
    return result;

base = int(input("base = "))
exponent = int(input("exponent = "))
result = powerOfNumber(base, exponent)
print(result)
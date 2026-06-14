number = 147
base = 8
result = 0
exponent = 0
while number:
    result += (number % 10) * base ** exponent
    exponent += 1
    number //= 10
print(result)
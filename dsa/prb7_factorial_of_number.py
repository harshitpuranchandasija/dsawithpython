number = 1
result = 1 if number > 0 else 'Not a valid number'
while number > 0:
    result = result * number
    number = number - 1
print(result)

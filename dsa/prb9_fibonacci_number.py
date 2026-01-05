no = 6
if no <= 2:
    print(f"Fibonacci of {no} is 1")
else:
    i = 3
    result = 0
    no1 = 1
    no2 = 1
    while i <= no:
        result = no1 + no2
        no1 = no2
        no2 = result
        i += 1
    print(f"Fibonacci of {no} is {result}")
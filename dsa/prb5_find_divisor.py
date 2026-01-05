def find_divisor(no):
    lst=list()
    i=1
    while i<=no//2:
        if no%i == 0:
            lst.append(i)
        i+=1
    lst.append(no)
    return lst

number = 6
lst_result = find_divisor(number)

print("%d number has divisors %s" % (number,lst_result))

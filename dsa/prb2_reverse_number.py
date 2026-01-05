
#Reverse a Number 

def reverse(number) -> int:
    reverse_no = 0
    while number > 0:
        reverse_no = reverse_no * 10 + number % 10
        number = number //10
    return reverse_no

number = 123
result=reverse(number)

print("Reverse of number %d is %d",(number,result))
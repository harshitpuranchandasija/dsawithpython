
def count_digits(no)->int:
    counter=0
    while no > 0:
        counter +=1
        no = no//10
    return counter
    

def is_arm_strong_number(no):
    #Count no of digits
    digits = count_digits(no)
    #Implement the logic to find Armstrong
    original_no = no
    result = 0
    while no > 0:
        last_digit = no%10
        result = result + (last_digit ** digits)
        no//=10
    print(f"Result is {result}")

    return True if original_no == result else False

number = 153

print("{} is {}".format(number,is_arm_strong_number(number)))





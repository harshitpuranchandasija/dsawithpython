#Count Number of Digits in a Given Number

number = 1345559977253647874682736425342345837
original_number = number
counter = 0
while number > 0:
    counter =counter + 1
    number = number//10
    print(number)

print("Total Digits in Number %d is %d" % (original_number, counter))

#TC O(N)
#SC O(1)
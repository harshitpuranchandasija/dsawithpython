arr = [1,1,1,1,1,1,1,2,2,2,2,2,3,4,5,6,7]

no=3
first=-1
last=-1

for i in range(0,len(arr)):
    if no == arr[i]:
        if first == -1:
            first=i
        last=i

print("first and Lst Occurenece is ",(first,last))

    
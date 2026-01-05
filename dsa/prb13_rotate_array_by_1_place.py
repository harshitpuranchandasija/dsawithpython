arr = [1,2,3,4,5,6,7]

#store last number
last_no=arr[-1]

for i in range(len(arr)-1,0,-1):
    arr[i] = arr[i-1]

arr[0] = last_no

#Print The Result
print(arr)

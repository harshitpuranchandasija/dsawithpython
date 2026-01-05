arr = [1,77,8,9,33,45,76,20]
max = float('-inf')
index = float('-inf')

for i in range(0,len(arr)):
    if arr[i] > max:
        max=arr[i]
        index=i

print("Maximum in Array is --> %d & Index is %d" % (max,index))

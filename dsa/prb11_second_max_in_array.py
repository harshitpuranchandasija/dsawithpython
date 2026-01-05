arr = [101,77,8,9,33,45,76,20]
max = float('-inf')
second_max= float('-inf')
index = float('-inf')

for i in range(0,len(arr)):
    if arr[i] > max:
        second_max=max
        max=arr[i]
        index=i
    elif arr[i] > second_max:
        second_max = arr[i]
        index=i

print("Second Maximum in Array is --> %d & Index is %d" % (second_max,index))

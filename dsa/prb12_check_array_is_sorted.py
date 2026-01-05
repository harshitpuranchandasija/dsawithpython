arr = [1,2,3,4,5,6,7,8]
is_sorted = True

for i in range(0,len(arr)-2):
    if not arr[i] < arr[i+1]:
        print("Array Is not Unsorted")
        break
else:
    print("Array is Sorted")
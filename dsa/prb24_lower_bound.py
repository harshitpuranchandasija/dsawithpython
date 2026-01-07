arr = [1,1,1,2,3,4,4,5,6,7]

l = 0
h = len(arr)-1

no=6

while l <=h:
    mid = (l+h)//2
    if arr[mid] >=no:
        h=mid-1
    else:
        l=mid+1

print("Lowerbound the no",l)

arr = [1,2,3,4,5,6,12]

l=0
h=len(arr)-1

no = 20
is_found=None
while l<=h:
    mid=(l+h)//2
    if arr[mid] == no:
        is_found=True
    if arr[mid] > no:
        h=mid-1
    else:
        l=mid+1

if is_found:
    print("Found")
else:
    print("Not Found")
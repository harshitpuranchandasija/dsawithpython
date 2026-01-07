arr = [1,3,4,5,6,7,8,9]

l=0
h=len(arr)-1

target=10

while l<=h:
    mid = (l+h)//2
    print(l,'+',h,'-->',mid,'-->',arr[mid])
    if arr[mid] >=target:
        h=mid-1
    else:
        l=mid+1

print("Index is ",l)
    

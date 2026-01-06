arr = [1,0,10,0,0,0,0,0,9,0,0]

#Counter Solution
lst=list()
count_zero = 0

for i in arr:
    if i == 0:
        count_zero +=1
    else:
        lst.append(i)

for _ in range(0,count_zero):
    lst.append(0)

print(lst)

#O(N+M)

#2 Pointer
for i in range(0,len(arr)):
    if arr[i] == 0:
        print(i)
        break

j=i+1

for j in range(j,len(arr)):
    if arr[i] != arr[j]:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
    j+=1

print(arr)
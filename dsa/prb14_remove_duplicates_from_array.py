arr = [1,1,2,2,3,3,4,4,5,5,6,7,8,8]

#Using Dictionary
result={}

for i in arr:
    if result.get(i,0) == 0:
        result[i] = 1


#Using set, Type Cast to set
result_set = set(arr)

print(dir(result_set))

#Without Using Extra Space
i=0
j=1

while(j < len(arr)):
    if arr[i] == arr[j]:
        pass
    else:
        i=i+1
        arr[i],arr[j]=arr[j],arr[i]
    j=j+1

print(arr[0:i+1])
arr =[1,1,0,1,1,1,1,0,0,0,1,1,1]
max_len = 0

count = 0
for i in range(0,len(arr)):
    if arr[i] == 1:
        count +=1
    else:
        if count > max_len:
            max_len = count
        count=0

print("List has %d consecutive 1" % max_len)
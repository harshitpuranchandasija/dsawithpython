arr = [5,10,-3,-1,-10,6]

result=[5,-3,10,-1,6,-10]

#Positive first and negative Later
pos=[]
neg=[]

for i in arr:
    if i >=0:
        pos.append(i)
    else:
        neg.append(i)

result = pos + neg

print("Rearranged List is %s" % result)


#Optimal Approach
arr = [5,10,-3,-1,-10,6]

arr_len = len(arr)

res = [0] * arr_len

p=0
n=1

for i in range(0,arr_len):
    if arr[i] > 0:
        res[p] = arr[i]
        p+=2
    else:
        res[n] = arr[i]
        n+=2

print("Re-arranged the List %s" % res)
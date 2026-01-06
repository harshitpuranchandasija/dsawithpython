
arr = [1,2,3,4,5,6,7,8,9]

#kth Place
k = 2

for _ in range(0,k):
    no = arr.pop(-1)
    print(no)
    arr.insert(0,no)

print(arr)

#Bettter Solution
k=2

arr = [1,2,3,4,5,6,7,8,9]

result = arr[len(arr)-k:len(arr)] + arr[0:len(arr)-k]

print(result)
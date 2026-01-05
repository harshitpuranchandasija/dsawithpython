arr=[*range(1,7)]

#reverse Indexing
print(arr[:1:-1])
print("*" * 50)

#Print In-Built
print(arr.reverse())
print(arr)
print("*" * 50)

#Using Loop

for i in range(len(arr)-1,-1,-1):
    print(arr[i])

    
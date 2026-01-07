arr = [1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,5,6,9]

no=3
counter=0

for i in arr:
    if i == no:
        counter+=1

print("Occurence of No {} of elements in array {}".format(no,counter))
from pprint import pprint
arr = [1,99,101,98,2,5,3,100,102]
counter=1
max_length = 0
no_dict = dict(map(lambda x: (x, 1), arr))

for i in range(0,len(arr)):
    no=arr[i]
    next_no=no+1
    while True:
        if next_no in no_dict:
            counter+=1
            next_no=next_no+1
        else:
            break
    if (counter > max_length):
        max_length = counter
    counter=1

print("Max is %d" % max_length)
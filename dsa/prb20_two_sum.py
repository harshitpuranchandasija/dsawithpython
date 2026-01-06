arr = [1,3,5,6,8,7]

no = 9

visited_no = {}

for i in range(0,len(arr)):
    check_no = no - arr[i]
    if check_no in visited_no:
        print((arr[i],check_no))
        break
    visited_no[arr[i]] = 0

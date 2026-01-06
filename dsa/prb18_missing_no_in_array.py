arr=[9,8,1,2,3,7,6,4,5,0]
sum_arr=0
sum_exist=0
for i in range(0,len(arr)+1):
    sum_arr+=i

for i in range(0,len(arr)):
    sum_exist +=arr[i]

print("sum_arr",sum_arr)
print("sum_exist",sum_exist)


#Missing Number
no = (sum_arr - sum_exist)
if no == 0:
    print("All Elements Present")
else:
    print("Number %d is Missing" % no)
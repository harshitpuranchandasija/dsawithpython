

def linear_search(no,arr):
    for i in range(0,len(arr)):
        if arr[i] == no:
            return 'there'
    return 'not'

if __name__ == '__main__':
    no=15
    arr = [1,2,3,4,5,6,7,8,10]
    is_there = linear_search(no,arr)

    print("%d is %s in list" % (no,is_there))
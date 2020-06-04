import math

def binsearch(arr,key):
    left = 0
    right = len(arr)-1

    while(left<=right):
        mid = math.floor(left+(right-left)/2)
        if(arr[mid]==key):
            return mid
        elif arr[mid]<key:
            left = mid+1
        else:
            right=mid-1
    return -1

arr = [1,2,3,4,5,6,7,10]
key = 5
result = binsearch(arr,key)
print("found at",arr[result])

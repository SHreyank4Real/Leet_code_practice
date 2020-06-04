def slide(arr,key):
    total_max = 0
    size = len(arr)
    cur_max=sum(arr[i] for i in range(key))
    for i in range(size-key):
        cur_max = cur_max-arr[i]+arr[i+key]
        total_max=max(cur_max,total_max)
    return total_max

arr = [2,4,6,1,9]
key = 3
ans = slide(arr,key)
print(ans)
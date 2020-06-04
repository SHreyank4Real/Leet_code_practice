def MaxSum(arr,key):
    max_sum = 0
    size = len(arr)
    for i in range(size-key+1):
        cur_max = 0;
        for j in range(key):
            cur_max +=arr[i+j]
        max_sum=max(cur_max,max_sum)
    return max_sum

arr = [80,-50,90,100]
key = 2
max = MaxSum(arr,key)
print(max)
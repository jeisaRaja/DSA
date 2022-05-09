
x = [3,5,7,10,11,14,16,34,57,69,80,86]

def binary(target):
    start = 0
    end = len(x)-1
    while start<=end:
        mid = start + (end-start)//2
        if target > x[mid]:
            start = mid+1
        elif target < x[mid]:
            end = mid-1
        else:
            return mid

    return end
        
target = 100
result = binary(target)

print(x[result])
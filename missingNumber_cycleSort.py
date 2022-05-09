def missing(array,n):
    i=0
    while i<len(array):
        if array[i]!=i and array[i]<len(array):
            temp = array[i]
            array[i]=array[temp]
            array[temp]=temp
        else:
            i=i+1
    for j in range(len(array)):
        if array[j]!=j:
            return j
    return n

x = [0,1,2,3,4,6,7]
n=8
print(missing(x,n))
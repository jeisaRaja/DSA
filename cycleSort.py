def cycle_sort(array):
    i = 0
    while i< len(array):
        if array[i]!=i+1:
            temp=array[i]
            array[i]=array[temp-1]
            array[temp-1]=temp
        else:
            i=i+1
    return array
array = [5,3,4,1,2,9,7,8,6]
print(cycle_sort(array))
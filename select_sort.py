def sort(array):
    n = len(array)
    for i in range(len(array)):
        index=0
        maxValue = array[0]
        for j in range(n):
            if array[j]>maxValue:
                maxValue=array[j]
                index = j
        temp = array[n-1]
        array[n-1]=maxValue
        array[index]=temp
        n=n-1
    print(array)
    

array = [3,1,5,6,2,2,7]
sort(array)
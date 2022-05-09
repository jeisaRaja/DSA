from abc import abstractproperty


def bubblesort(array):
    n2 = len(array)-1
    for i in range(len(array)):
        swapped = False
        for j in range(n2):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]= temp
                swapped = True
            elif swapped == False:
                return array
            print(f'{i} and {j}')
        n2=n2-1
    return array




array = [6,5,4,2,1,8,9]

print(bubblesort(array))
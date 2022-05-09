letters = ["c","f","j"]       
target = 'a' 
def binary(target):
    start = 0
    end = len(letters)-1
    n = len(letters)
    while start <= end:
        m = start + (end-start)//2
        if letters[m] > target:
            end = m-1

        else :
            start = m+1

    return letters[start%len(letters)]

print(binary(target))
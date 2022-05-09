def pattern(n):

    for i in range(1,2*n):
        print(i)
        cols = (2*n)-i if i>n else i
        for j in range(cols):
            print(i, end=" ")
        print("")
pattern(3)
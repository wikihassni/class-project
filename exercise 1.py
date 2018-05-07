def F():
    a,b = 0,1
    print(a,b)
    for i in range (0,99):

        a, b = b, a + b
        print(b)

F()

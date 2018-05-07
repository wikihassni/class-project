def largestprime():
    number=600851475143
    factor=2
    primelist=[]
    while number>1:
        if number % factor ==0:
            primelist.append(factor)
            number=number/factor
        else:
            factor+=1
    print(primelist)
largestprime()

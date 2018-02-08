def Atm(n):
    g = 'give :'
    l = [100,50,10,5]
    nu= 0
    while n >5 :
        while n > l[nu]:
            print g + str(l[nu])
            n -= l[nu]
        nu +=1
    return g +str(n)
print Atm(277)
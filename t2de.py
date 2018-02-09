<<<<<<< HEAD

def Atm(request):

  giveString = 'give :'
  validPapers = [100, 50, 10, 5]
  validPaperIndex = 0

  while request > 5:

      while request > validPapers[validPaperIndex]:
          print(giveString + str(validPapers[validPaperIndex]))
          request -= validPapers[validPaperIndex]

      validPaperIndex += 1

  return(giveString + str(request))


print(Atm(277))
=======
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
>>>>>>> master

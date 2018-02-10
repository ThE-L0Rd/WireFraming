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



def withdraw(balance,request):
    delet = request
    if balance == 0:
        print "You don't have any papers :|"
    elif balance < request:
        print "You don't have enough papers :( "
    giveString = 'give :'
    validPapers = [100, 50, 10, 5]
    validPaperIndex = 0
    if request =>50 and request <=99 :
        validPaperIndex = 1
    elif request =>5 and request <=49 :
        validPaperIndex = 1
    if request >= 5:
        while request >= 5:

            while request > validPapers[validPaperIndex]:
                print(giveString + str(validPapers[validPaperIndex]))
                request -= validPapers[validPaperIndex]

            validPaperIndex += 1

        print (giveString + str(request))
    return balance - delet

balance = 500
balance = withdraw(balance,277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)

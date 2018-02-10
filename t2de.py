def requestPapers(amount,request):
    #Until he deduct the amount to be withdrawn from the card
    delete = request
    giveString = 'give :'
    #List of valid papers
    validPapers = [100, 50, 10, 5]
    #to use it in the loop underneath
    validPaperIndex = 0
    #So make sure the value of the paper that will come out from Atm
    if request >=50 and request <=99 :
        validPaperIndex = 1
    elif request >=10 and request <=49 :
        validPaperIndex = 2
    elif request >=5 and request <=9 :
        validPaperIndex = 3
    while request >= 5:

        while request >= validPapers[validPaperIndex]:
            print(giveString + str(validPapers[validPaperIndex]))
            #The amount is deducted from the request in each cash-out process
            request -= validPapers[validPaperIndex]
        #To reduce the value of the papers that will be drawn until the balance ends
        validPaperIndex += 1
    #To extract the rest of the required amount
    if request !=0 :
        print (giveString + str(request))

    print  amount - delete
    return amount - delete

def chack(amount,request):

    if amount < request :
        print "you don't have enough money!"
        return

    elif request == 0 :
        print "pleas enter valid request "
        return

    else :
        return requestPapers(amount,request)


balance = 500
balance = chack(balance,277)
balance = chack(balance, 30)
balance = chack(balance, 5)
balance = chack(balance, 500)


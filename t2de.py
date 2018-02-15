class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list=[]

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print(withdrawal)

    def withdraw( self, request):
        #A comma between the parts
        comma ="+----------------------+"
        print "Welcome to " + self.bank_name
        print "Current balance = " + str(self.balance)
        print comma
        if self.balance < request :
            print "you don't have enough money!"
            return

        elif self.balance == 0 :
            print "pleas enter valid request "
            return
        else :
            #Until he deduct the amount to be withdrawn from the card
            delete = request
            giveString = 'give :'
            #List of valid papers
            validPapers = [100, 50, 10, 5]
            #to use it in the loop underneath
            validPaperIndex = 0
            #So make sure the value of the paper that will come out from Atm
            if request >=100 :
                validPaperIndex = validPaperIndex
            elif request >=50 :
                validPaperIndex = 1
            elif request >=10:
                validPaperIndex = 2
            elif request >=5:
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

            self.balance -=delete
            self.withdrawals_list.append(delete)
            print self.balance
            print comma

balance1 = 500
#balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
#atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(200)

#atm2.withdraw(100)
#atm2.withdraw(2000)

atm1.show_withdrawals()



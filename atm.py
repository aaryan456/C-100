class ATM(object):
    
    def __init__(self,company,transactionlimit):
        self.company = company
        self.transactionlimit = transactionlimit
    
    def amount(self):
        print("Max Amount that can be transacted = 2000")

    def Debited(self):
        print("Given")
    
bank = ATM("transactionlimit",8000)

print(bank.amount())
print(bank.Debited())

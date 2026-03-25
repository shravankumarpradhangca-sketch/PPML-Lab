class bank:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def depoist(self,amount):
        self.balance+=amount
        print("Depoisted :",amount)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=self.balance
            print("withdraw :",amount)
        else:
            print("\n insuffiect balance.")
    def display(self):
        print("\n Account Number :",self.account_number)
        print("\n Account Holder : ",self.account_holder)
        print("\n Balance :",self.balance)
acc1=bank(101,"Abinas",5000)
acc1.depoist(2000)
acc1.withdraw(1500)
acc1.display()
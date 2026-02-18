class Bank:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    def display(self):
        print("name:",self.name)
        print("acc_no:",self.acc_no)
        print("balance:",self.balance)
    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance-=amount
            print("u r amount sucessfully debited",amount)
        else:
            print("insuffient")
    def deposite(self,amount):
        self.balance+=amount
    def show_balance(self):
            print("balance:",self.balance)
h1=Bank("harsha",171,20000)
h1.display()
h1.deposite(1000)
h1.show_balance()
h1.withdraw(2000)
h1.show_balance()



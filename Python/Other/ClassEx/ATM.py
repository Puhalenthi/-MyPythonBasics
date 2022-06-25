class ATM():
    def __init__(self, bal = 100):
        self.bal = bal
        self.main()
    
    def main(self):
        while True:
            print('''
                    Main Menu
                    1: Check Balance
                    2: Withdraw
                    3: Deposit
                    4: Exit
                ''')
            a = int(input('Enter a choice:  '))
            if a == 1:
                print(self.checkbalance())
            elif a == 2:
                print(self.withdraw())
            elif a == 3:
                print(self.deposit())
            elif a == 4:
                break
            else:
                print('Enter a valid response')
    
    def checkbalance(self):
        return 'The balance is {}'.format(self.bal)
    
    def withdraw(self):
        self.bal -= int(input('Enter an amount to withdraw: '))
        return self.checkbalance()
    
    def deposit(self):
        self.bal += int(input('Enter an amount to deposit:  '))
        return self.checkbalance()

a = ATM()
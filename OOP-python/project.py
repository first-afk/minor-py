class BankAccount:
    def __init__(self, name, type, acctNumber, balance) -> None:
        self.acctName = name
        self.accType = type
        self.acctNumber = acctNumber
        self.balance = balance
        self.transactionHistory = []

    def deposit_money(self, amount):
        amount = int(amount)
        self.balance += amount
        self.transactionHistory.append(('Credit', amount))
        print(f'Transaction successful, you deposited {amount}')

    def withdraw_money(self, amount):
        amount = int(amount)
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            self.transactionHistory.append(('Debit', amount))
            print(f'Transaction successful, you withdrew {amount}')

    def check_balance(self):
        print(self.balance)

    def transaction_history(self):
        for transact in self.transactionHistory:
            print(transact)

# acc = BankAccount('Esther', 'Savings', 239080, 0)
# acc.deposit_money(500)             
# acc.check_balance()    
# acc.withdraw_money(200)   
# acc.check_balance()      
# acc.transaction_history()        

def main():
    bank_users = []

    while True:
        print()
        print()
        print('Welcome to your bank')
        print('What woulld you like to do?')
        print('1, Create an account')
        print('2, Deposit money')
        print('3, Withdraw money')
        print('4, Check balance')
        print('5, Check transaction history')
        print('6, Exit')
        choice = input('What would you like to do?: ')
        if choice == '1':
            name = input('Enter your name: ')
            acctType = input('Enter your account type (savings/current): ')
            acctNumber = int(input('Enter your account number: '))
            balance = 0
            newAcct = BankAccount(name, acctType, acctNumber, balance)
            bank_users.append(newAcct)

        elif choice == '2':
            acct = int(input('Enter your account number: '))
            amount = int(input('Enter the amount to deposit: '))
            if len(bank_users) >=1:
                for user in bank_users:
                    if user.acctNumber == int(acct):
                        user.deposit_money(amount)
                        break
                    else: 
                        print('Could not find account')
            else:
                print('Name not found')
        elif choice == '3':
            acct = int(input('Enter your account number: '))
            amount = int(input('Enter the amount to deposit: '))
            if len(bank_users) >=1:
                for user in bank_users:
                    if user.acctNumber == int(acct):
                        user.withdraw_money(amount)
                        break
                    else: 
                        print('Could not find account')
            else:
                print('Name not found')
        elif choice == '4':
            acct = int(input('Enter your account number: '))
            if len(bank_users) >=1:
                for user in bank_users:
                    if user.acctNumber == int(acct):
                        print('Balance: ')
                        user.check_balance()
                        break
                    else: 
                        print('Could not find account')
            else:
                print('Name not found')
        elif choice == '5':
            acct = int(input('Enter your account number: '))
            if len(bank_users) >=1:
                for user in bank_users:
                    if user.acctNumber == int(acct):
                        print('Transaction history: ')
                        user.transaction_history()
                        break
                    else: 
                        print('Could not find account')
            else:
                print('Name not found')
        elif choice == '6':
            break

main()
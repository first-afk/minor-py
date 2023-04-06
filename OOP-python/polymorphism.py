class Animal:
    def type(self):
        print('this is an animal')

    def legs(self):
        print('has 4 legs')

class Spider(Animal):
    def legs(self):
        print('has 8 legs')

s = Spider()
s.type() 


# project
# create a bsnk account management from system that allows users to create and manage their bank accounts. the system should allow users to  perform basic banking iperations like depositing and withdrawing money, checkming balance and viewing transaction history
# create a bank account class that will have attributes: account number, account holder name, account type(savings or checking), and balance
#  define a constructor method that will initialize the account attributes when a new object is created
#  define methods for depositing amd withdrawing money from the account.these methods should uodate the balance attribute accordingly
# define a method for checking the current balance of the account
# define a method for displaying the transaction history of the account
# create a main function that will allow users to create new accounts and perform banking operations on their accounts


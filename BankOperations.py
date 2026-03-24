uniID = 0

import random as rand

class bankAccount:
    def __init__(self, owner, balance):
        global uniID
        self._owner = owner
        self._balance = balance
        self._ID = uniID
        uniID = uniID + 1
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def ID(self):
        return self._ID
    
    def showAccount(self):
        print(f"Account ID: {self._ID}      Account owner: {self.owner}")

    def requestBalance(self):
        return self._balance

    def requestAccount(self):
        return f"Account ID: {self._ID}     Account owner: {self.owner}     Balance = ${self._balance}"
    
    def __str__(self):
        return self.requestAccount()
    
    def __repr__(self):
        return self.__str__()
    
    @staticmethod
    def logTransaction(function):
        def wrapper(self, amount):
            print(f"Proceeding with operation {function.__name__}")
            function(self, amount)
            print(f"Current Balance is: ${self._balance}")

        return wrapper
    
    def isBalanceCritical(self):
        if self._balance <=0:
            return True
        else:
            return False
        
    @logTransaction
    def deposit(self, amount):
        self._balance += amount
        balCheck = self.isBalanceCritical()
        if amount > 100:
            self._balance += (amount * (5/100)) 
            print(f"You have received 5% deposit bonus!")
        if balCheck == True:
            print(f"Warning: Bank balance is low")

    @logTransaction
    def withdraw(self, amount):
        self._balance -= amount
        if self._balance < 0:
            self._balance -= 10
            print(f"Negative balance penalty, deducted $10")

    @classmethod
    def accountGenerator(cls, number):
        if number < 3:
            number = 3
        
        for i in range(number):
            print(f"Please enter account holder's name: ")
            yield cls(input(), rand.randint(50, 200))


userList = []

accNumber = 3
x = bankAccount.accountGenerator(accNumber)

for i in x:
    userList.append(i)

chosenAccount = 0

while True:
    print(f"\nChoose desired operation: ")
    print(f"1. Display accounts     2. Choose Account     3. Withdraw from chosen      4. Deposit in Chosen")
    print(f"5. View balance of the chosen account      6. Exit")

    try:
        choice = int(input())
    except ValueError:
        print("Please type in a correct value")
        continue

    if choice == 1:
        for user in userList:
            print(user)

    elif choice == 2:
        print(f"Enter account ID")
        try:
            chosenAccount = int(input())
            if chosenAccount >= accNumber or chosenAccount < 0:
                chosenAccount = 0
                print(f"Selection has been reset due to an invalid ID input")
                continue
        except ValueError:
            print(f"Please enter a valid number")
            continue
    
    elif choice == 3:
        print("Enter the amount you wish to withdraw:")
        try:
            userList[chosenAccount].withdraw(int(input()))
        except ValueError:
            print(f"Please input a valid amount")
            continue
    
    elif choice == 4:
        print(f"Enter the amount you wish to deposit:")
        try:
            userList[chosenAccount].deposit(int(input()))
        except ValueError:
            print(f"Please enter a valid amount")
            continue

    elif choice == 5:
        print(f"Account balance is ${userList[chosenAccount].balance}")

    elif choice == 6:
        print(f"Exiting...")
        break

    else:
        print("Please input a correct option")

    
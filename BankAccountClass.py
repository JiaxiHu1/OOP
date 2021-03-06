# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, bal):
        self.__balance = bal

        #so we only have ONE attribute which is the balance from the user 


      # The deposit method makes a deposit into the
      # account.

#function - deposit is mutator need more information and will change 
#mutator method is a set method 
#accessor method is a get method - only need self - get method 
#self-attribute - instance attribute - belongs to a specific instance of a class 

    def deposit(self, amount):
        self.__balance += amount

      # The withdraw method withdraws an amount
      # from the account.

    def withdraw(self, amount):
      #test that we don't want amount less than 0 
      if amount <= 0:
        print("You Fool!")
      else: 
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

      # The get_balance method returns the
      # account balance.

    def get_balance(self):
        return self.__balance


    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')

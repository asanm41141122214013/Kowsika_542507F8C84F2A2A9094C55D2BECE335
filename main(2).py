class bank_account:

  def __init__(self,account_number,
               account_holder_name,account_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=account_balance

  def deposit_money(self,amount):
    if amount > 0:
      self.__account_balance += amount 
      print("Deposited:₹{} ;balance:₹{}".format(amount,
                                self.__account_balance))
    else:
      print("Invalid deposite money")
      
  def withdraw_money(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("withdraw:₹{} ; new balance:₹{}".format
                        (amount,self.__account_balance))
    else:
      print("Invalid withdrawal money")

  def display_balance(self):
    print("account balance for {} (account no.{}) is ₹ {}".format(self.__account_holder_name,
         self.__account_number,self.__account_balance))


account=bank_account(account_holder_name="shaf",
                     account_number="123456",
                     account_balance=5000.0)
account.display_balance()
account.deposit_money(500.0)
account.withdraw_money(2000.0)
account.display_balance()
class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()

    def withdraw(self, amount):
        if self.__balance < amount:
            print("残高が足りません")
        else:
            self.__balance -= amount
            self.show_balance()

    def show_balance(self):
        print(f"残高は{self.__balance}円です")


myaccount = Account(10000)
myaccount.deposit(1000)
myaccount.withdraw(3000)
# print(myaccount.__balance)
myaccount.__balance = 1000
# ↑ 書き換えではなく、新しい属性が作成されている
print(myaccount.__balance)
myaccount.show_balance()
print(dir(myaccount))

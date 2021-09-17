import time


class Account:
    account_number = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.account_number
        self.transaction_history = []
        Account.account_number += 1

    def withdraw(self, price):
        price = abs(price)
        if self.balance >= price:
            self.balance -= price
            self.add_transaction(-price)
            print(f"口座名:{self.name} {price}円引き落とします。残高は{self.balance}円です。")
        else:
            print("残高が不足しています")

    def deposit(self, price):
        price = abs(price)
        self.balance += price
        self.add_transaction(price)
        print(f"口座名:{self.name} {price}円を振り込みます。残高は{self.balance}円です。")

    def add_transaction(self, price):
        transaction = {
            'withdraw/deposit': price,
            'new_balance': self.balance,
            'time': Account.get_time_str()
        }
        self.transaction_history.append(transaction)

    @staticmethod
    def get_time_str():
        current_time = time.localtime()
        ret = "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)
        return ret

    def show_transaction_history(self):
        for transaction in self.transaction_history:
            transaction_list = []
            for k, v in transaction.items():
                transaction_list.append(f"{k}: {v}")
            print(", ".join(transaction_list))


account1 = Account("Account1", 30000)

account1.deposit(50000)
account1.withdraw(35000)
account1.withdraw(20000)

print(account1.transaction_history)
account1.show_transaction_history()

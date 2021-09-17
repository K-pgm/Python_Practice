import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ※クラスメソッドにしている理由は、継承を学ぶと理解できる
    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()

        # 年、月、日から年齢を算出
        # if (today.tm_mon, today.tm_mday) < (month, date):
        #     age = today.tm_year - year -1
        # else:
        #     age = today.tm_year - year - 0

        # ↑ 1,0 は True, Falseと同じのため、以下のように書き直せる
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))

        return cls(name=name, age=age)


john = Person("John", 20)
emma = Person.create_from_dob('Emma', 1989, 9, 14)
print(john.name)
print(emma.age)
print(type(john))

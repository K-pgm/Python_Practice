from builtins import print


class Person:

    num_legs = 2
    count = 0

    # constructor (__new__)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking with {Person.num_legs} legs")

    def run(self):
        print(f"{self.name} is running with {Person.num_legs} legs")


john = Person("John", 28, 'male')
taro = Person("Taro", 18, 'male')
emma = Person("Emma", 40, 'female')

# インスタンス変数
# 「.」に続けてアクセス可能
print(john.name)
john.age = 29
print(john.age)

# インスタンスメソッド
john.walk()
taro.run()

print(john.num_legs)
print(taro.num_legs)
print(Person.num_legs)
print(Person.count)
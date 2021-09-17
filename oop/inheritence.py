class Animal(object):

    def __init__(self, name):
        self.name = name
        print("Anima init is called!!")

    def breathe(self):
        print(f"{self.name} is breathing")


class Dog(Animal):

    def __init__(self, name):
        # スーパークラスのinitを呼び出す
        super().__init__(name=name)
        print("Dog init is called")


pochi = Dog("pochi")
print(pochi.name)
pochi.breathe()

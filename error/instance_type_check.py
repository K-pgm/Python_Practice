class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


def walk_with_me(animai: Animal) -> None:
    # ※↓ Animalのサブクラスの場合、Falseとなってしまう
    # if type(animai) is Animal:
    # ※↓ Pythonは型ではなく振る舞いで判定するほうがbetter
    # if isinstance(animai, Animal):
    # ※↓ 属性を取得できる。ただしインスタンス変数の可能性もあるのでcallableも挟む
    method = getattr(animai, 'walk', None)
    if callable(method):
        animai.walk()
    else:
        raise TypeError(f"{type(animai).__name__}は散歩(walk)できません")


if __name__ == "__main__":
    pochi = Dog("Pochi")
    walk_with_me(pochi)
    walk_with_me("pochi")

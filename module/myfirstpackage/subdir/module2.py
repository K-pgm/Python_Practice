from .module3 import myfunc3
# from ..subdir import module3


def myfunc():
    print("This is myfunc from module2!")


def myfunc2():
    print("This is myfunc2 from module2!")
    myfunc3()

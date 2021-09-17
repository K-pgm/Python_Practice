class MyClass:

    classmethod_count = 0

    def mymethod(self):
        print("This is normal method!")

    # celfを扱わない
    @staticmethod
    def _mystaticmethod():
        print("This is staticmethod!")

    @classmethod
    def _myclassmethod(cls):
        cls.classmethod_count += 1
        print(f"This is classmethod and now the count is {cls.classmethod_count}")


c = MyClass()
c.mymethod()
MyClass._mystaticmethod()
MyClass._myclassmethod()
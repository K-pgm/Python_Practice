my_variable = "This is global variable!!"


def myfunc():
    print("This is my function!!")


def anotherfunc():
    print("This is another function!!")


# 外部からのアクセスをしてほしくないものに"_"をつける
# ※Pythonとして制御してくれるわけではない
def _dontImportfunc():
    print("dont")


if __name__ == "__main__"   :
    print(f"mymodule.__name__: {__name__}")

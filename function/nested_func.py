# 関数の中で関数を定義
def outer():
    def inner():
        print("This is inner function")
    inner()

outer()
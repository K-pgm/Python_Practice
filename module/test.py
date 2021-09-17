def greeting(func):
    def inner(*args, **kwargs):
        print("デコレートスタート")
        func(*args, **kwargs)
        print("デコレートエンド")
    return inner

@greeting
def say_name(name):
    print(f"I'm {name}")


say_name("taro")

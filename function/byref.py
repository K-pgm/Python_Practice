# 参照渡し <->値渡し
def add_nums(a, b):
    a += 10
    return a + b

one =1
two = 2
print(add_nums(one, two))
print(one)
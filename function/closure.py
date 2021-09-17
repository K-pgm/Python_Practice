# Closure

# 関数もオブジェクト
def compute_square(num):
    return num * num


f = compute_square
print(type(f))
print(f(10))


# 関数も引数として渡せる
def execute_fun(func, param):
    return func(param)


print(execute_fun(f, 10))


# 関数をreturnする
def retrun_func():
    def inner_func():
        print("This is an inner function")

    return inner_func


f = retrun_func()
print(f)


# Closure 状態をキープした関数を作ることができる
# 状態が静的
def power(exponent):
    def inner_power(base):
        return base ** exponent

    return inner_power


power_four = power(4)
print(power_four(3))

power_five = power(5)
print(power_five(2))


# 状態が動的
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)

    return inner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))

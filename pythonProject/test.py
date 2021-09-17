import time


def fibonacchi_self(index):
    if index < 2:
        return index
    else:
        return fibonacchi_self(index - 1) + fibonacchi_self(index - 2)


def fibonacci(index):
    if index < 2:
        return index
    else:
        nums = [0, 1]
        for i in range(2, index + 1):
            num = nums[i - 2] + nums[i - 1]
            nums.append(num)
    return nums[i]


def fibonacci_sample(n):
    if n < 2:
        return n
    else:
        n_2 = 0
        n_1 = 1
        for _ in range(n - 1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


index = 100000

# now1 = time.time()
# print(fibonacchi_self(index))
# now2 = time.time()
# print(now2 - now1)

# 自作関数のほうが、サンプル関数より３倍かかる　※20000以上
now1 = time.time()
print(fibonacci(index))
now2 = time.time()
print(now2 - now1)


now1 = time.time()
print(fibonacci_sample(index))
now2 = time.time()
print(now2 - now1)
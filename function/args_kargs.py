# args
def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num


average = get_average(1, 2, 3, 4, 5, 6, 7, 8, )
print(average)


def kawrgs_func(**kwargs):
    print(type(kwargs))
    print(kwargs)

kawrgs_func(param1= 10, param2=20)

a = {'a':1, 'b':2}
b = {'c':3, 'd':4}
c = {**a, **b}
print(c)
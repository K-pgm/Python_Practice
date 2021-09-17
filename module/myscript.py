# 標準ライブラリ、サードパーティのライブラリ、自分たちのライブラリ、ローカルのライブラリ
import sys

sys.path.append("/Users/yanya/PycharmProjects/function/")
import docstring
# import mymodule
from mymodule import myfunc, my_variable, anotherfunc

# from mymodule import *
# ↑便利だが非推奨

# print(mymodule.my_variable)
# mymodule.myfunc()
# myfunc()
# print(my_variable)


for path in sys.path:
    print(path)

print(docstring.diviend(1, 1))

# 変数定義
# correct
x = 1
y = 1
# wrong
xxxx        = 1
y           = 1

# 関数の引数の「=」にはスペース不要
def complex(real, imag=0.0):
    return magic(r=real, i=imag)


# operatorの周りにスペース1個 , operatorにpriorityがある場合にはスペースをなくす
x = x + 1
x += 2
x = x*x + y*y
x = (y+1) * (y-1)

# カンマの後ろにはスペースを入れる ※カンマの後ろに閉じカッコが来る場合はスペース不要
range(1, 11)
a = [1, 2, 3, 4]
foo = (0,)

# バージョン管理で項目追加分だけdiffとなるよう、あえて最後の項目にもカンマをつける
FILLES = [
    'setup.cfg',
    'tox.ini',
    'tox.ini',
]

# 行の折り返し 80文字とされているが、それより長くなっても良い
foo = long_function_name(var_one, var_two,
                         var three, var_four)

foo = lng_function_name(
    var_one, var_two,
    var_three, var_four
)

# correct
def long_function_name(
        var_one, var_two, var_three, var_four):
    print(var_one)

# wrong
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

# '\'で区切って改行する
print("このように表示する文章が長かったりする場合は\
バックスラッシュで区切ると改行できる")
# correct
a = 1000000000000000000 \
    + 10000000000000000 \
    + 10000000000 \
    + 10000000

# wrong
a = 100000000000000 +\
    1000000000000 +\
    1000000000

# 関数間は2行空ける
def func():
    pass


def func2():
    pass

# 同じクラス内の関数は1行空ける
class MyClass:
    def __init__(self):
        pass

    def method(self):
        pass

# importのStyle ファイルの先頭に書く
# correct
import os
import sys

# wrong
import os, sys

# from の場合は複数を1行に書いても良い
from subprocess import Popen, PIPE

# 順番
# 1.Standard library (time, sys)
# 2.Third party (numpy, pandas)
# 3.Our library
# 4.Local library
# それぞれ1行空ける (abc順)

# absolute import
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

# 長過ぎる場合は相対でも可

# コメント
# ・コメントは常に最新にする　コメントとコードの中身が異なるなら、コメントはないほうがマシ
# ・なるべく英語で書く　絶対に日本語がわからない人が読まないなら日本語でもOK
# ・書くときは文章で書くのが望ましい
# ・書くときは文章で書くのが望ましい
# ・#のあとに半角スペースを入れる
# ・インラインコメントはコードのあとに半角スペースを2つ入れる
# ・Docstringは基本的にすべてのmodule, function, class, methodにつける(non publicな外からアクセスしない関数には不要)
# ・そのコードが「何をしているか」より「なぜそう書いたか」のほうが有益

# wrong
balance = 10000
# 残高が引き落とし額より大きければ
if balance < withdraw:
    pass
# correct
# 残高が足りない場合を考慮する
if balance < withdraw:
    pass

# 命名規則
# 変数名や関数 スネークケース
# クラス名 キャメルケース
# モジュールやパッケージ名 なるべく短いlower caseで、必要であればsnake_case

# アンダースコア
# _XXX: internal use only(non public)の意味
# XXX_: Pythonですでに使われている単語を使いたいとき
# __XXX: クラスの属性として使うことで名前修飾される
# __XXX__: magic methodと呼ばれるもので、Pythonが特別に設定しているもの。開発者が定義することはないう
#　　　　　　(overrideすることはある)
# _:最近実行した戻り値や、iteration時に使わない変数
for _ in range(10):
    print("hello")

# l, I , 0 一文字の変数は見間違えるので使わない

# Constantsは大文字のsnakecaseを使う

# Return
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        # returnを書くならNoneまで書く
        return None

# オブジェクトタイプの確認はisinstance()を使う
# correct
if isinstance(obj, int)

# wrong
if type(obj) is type(1)

# Booleanに比較演算子を使わない
bool_var = True

# correct
if vool_var:
# wrong
if bool_var == True

# type hint
def greeting(name: str) -> str:
    return "Hello" + name
# 一つでもhintをつけたらすべてにつける
# Pythonがtypeのチェックをしてくれるわけではない
# Pythonは動的型付け言語であることを意識
# type hintを強制したり、命名規約に入れるべきではない







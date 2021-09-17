# import re
#
# # Regular Expression (正規表現　通称RegEx)
#
# email = "myemail@gmail.com"
#
# # マッチしたらオブジェクトを返す　しなければNoneを返す
# matched = re.search('@\w+\.', email)
#
# if matched:
#     print(matched)
#     print("Matched")
# else:
#     print("Not found")
#
# # metacharacter
# # []
# print(re.search('[abc]', 'apple'))
# print(re.search('[a-c]', 'refs'))
#
# # ^ 最初の文字
# print(re.search('^[0-9]', '1test0'))
#
# # {n} n回リピート
# print(re.search('^[0-9]{2}', '21/3/31'))
#
# # {n, m} 最低n回、最高m回リピート
# print(re.search('^[0-9]{2,4}', '21/3/31'))
#
# # $ 最後の文字
# print(re.search('[0-9]{2}$', '2021/3/1'))
#
# # * 左のパターンを0回以上繰り返す
# print(re.search('a*b', 'abc'))
#
# # + 左のパターンを1回以上繰り返す
# print(re.search('a+b', 'bc'))
#
# # ? 左のパターンを0回か1回繰り返す
# print(re.search('ab?c', 'ac'))
#
# # | or
# print(re.search('ablc|012', '01'))
#
# # () グループ
# print(re.search('te(s|x)t', 'test'))
#
# # . 任意の一文字
# print(re.search('h.t', 'hit'))
#
# # \ エスケープ
# print(re.search("h\.t", 'hit'))
#
# # \w [a-zA-Z0-9] すべてのアルファベット 数字及びアンダースコア
# print(re.search('h\wt', 'h0t'))
#
import re

# challenge1
# while True:
#     birthday = input("生年月日を入力してください yyyy/mm/dd")
#     mathed = re.search('^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[01])$', birthday)
#     if mathed:
#         break
#
# print("OK")


# challenge2

pattern_email = '^[\w\.\-]+@[a-zA-Z]+\.[a-zA-Z]+$'
while True:
    email = input("メールアドレスを入力してください ****@****.***")
    matched = re.search(pattern_email, email)
    if matched:
        break

print("OK")

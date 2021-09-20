# for
# with open("pep8_introduction.txt") as f:
#     for line in f:
#         print(line, end="")

# .read()でファイルの中身すべてを一つのstringとして返す
# with open("pep8_introduction.txt") as f:
#     print(f.read())

# .readline()で一行ずつ取得しstringで返す
# ファイルが大きい場合はこの方法がよい
# with open("pep8_introduction.txt") as f:
#     line = f.readline()
#     while line:
#         print(line, end="")
#         line = f.readline()

# .readlines()ですべての行をListで返す
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line, end="")
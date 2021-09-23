from builtins import iter

fruits = ['apple', 'lemon', 'peach']

# next(fruits)

# forでまわすものはすべてiterable
# iteratorは__next__()と__iter__()が正しく実装されたオブジェクト

fruits_iterator = iter(fruits)
print(next(fruits_iterator))
print(next(fruits_iterator))
print(id(fruits_iterator))
print(id(iter(fruits_iterator)))

print("=" * 50)
print(next(fruits_iterator))
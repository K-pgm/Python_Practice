import sys

# リスト内包表記
square_list = [num * num for num in range(10)]
# print(square_list)
print(sys.getsizeof(square_list))

# generator ※メモリが大きくなりそうなときはこちらを使う
even_squares = (num * num for num in range(10))
print(sys.getsizeof(even_squares))
print(even_squares)
print(next(even_squares))
print(next(even_squares))
print(next(even_squares))
print(next(even_squares))

even_squares_gen = (num * num for num in range(10) if num % 2 == 0)
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
print(next(even_squares_gen))
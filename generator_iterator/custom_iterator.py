class MyIterator:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        num = self.current
        self.current += 1
        return num

    def __iter__(self):
        return self


myiterator = MyIterator(10)


# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))


class Even:
    def __init__(self, num):
        self.current = num

    def __next__(self):
        if self.current < 2:
            raise StopIteration
        elif self.current % 2 == 0:
            num = self.current
            self.current -= 2
            return num
        else:
            self.current -= 1
            return self.__next__()

    def __iter__(self):
        return self


if __name__ == "__main__":
    myeven = Even(10)
    print(next(myeven))
    print(next(myeven))
    print(next(myeven))
    print(next(myeven))
    print(next(myeven))
    print(next(myeven))

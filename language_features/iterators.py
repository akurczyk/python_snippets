class PowTwo:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= self.limit:
            raise StopIteration

        v = self.i ** 2
        self.i += 1
        return v


for i in PowTwo(10):
    print(i)


iterator = iter(PowTwo(2))
print(next(iterator))
print(next(iterator))
print(next(iterator))

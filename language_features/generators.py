def generator(limit=0):
    i = 0
    while i < limit:
        yield i ** 2
        i += 1


for i in generator(10):
    print(i)


iterator = generator(2)
print(next(iterator))
print(next(iterator))
print(next(iterator))

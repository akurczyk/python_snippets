def generator(limit):
    i = 0
    while i < limit:
        yield i
        i += 1


for i in generator(10):
    print(i)

# iterator = generator(2)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

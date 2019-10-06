aaa = {x for x in range(0, 20)}
bbb = {x for x in aaa if x % 2}
ccc = {x for x in range(10, 30)}

print(aaa.issuperset(bbb))
print(bbb <= aaa)

print(bbb.issubset(bbb))
print(aaa >= bbb)

print(aaa.union(ccc))  # sum
print(aaa | ccc)

print(aaa.intersection(ccc))
print(aaa & ccc)

print(aaa.difference(ccc))
print(aaa - ccc)

print(aaa.symmetric_difference(ccc))
print(aaa ^ ccc)

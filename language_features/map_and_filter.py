from pprint import pprint

aaa = [x for x in range(0, 10)]
bbb = list(map(lambda x: x*x, aaa))
ccc = [x*x for x in aaa]  # equivalent

pprint(bbb)
pprint(ccc)

aaa = [x for x in range(0, 20)]
bbb = list(filter(lambda x: x > 10, aaa))
ccc = [x for x in aaa if x > 10]  # equivalent

pprint(bbb)
pprint(ccc)

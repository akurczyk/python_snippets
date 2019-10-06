from pprint import pprint

aaa = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
bbb = [x for x in range(0, 20)]
ccc = list(zip(aaa, bbb))
pprint(ccc)

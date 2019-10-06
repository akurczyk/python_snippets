# list_ = [expression
#          for item in collection
#          if condition]

list_ = [x*x for x in range(0, 20) if x >= 5]
dict_ = {x: x*x for x in range(0, 20) if x >= 5}
set_ = {x*x for x in range(0, 20) if x >= 5}
generator = (x*x for x in range(0, 20) if x >= 5)

aaa = [x for x in range(0, 10)]
bbb = [x for x in aaa if x % 2]
ccc = [x*x for x in bbb]

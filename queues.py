# Queues support multi threading :-)
# For use with multiprocessing module there is another Queue implementation
# located in the multiprocessing module.

from queue import LifoQueue  # deque based
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')
while not s.empty():
    next_item = s.get()
    print(next_item)

from queue import Queue  # deque based
q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')
while not q.empty():
    next_item = q.get()
    print(next_item)

from queue import PriorityQueue  # binary heap based
p = PriorityQueue()
p.put((2, 'code'))
p.put((1, 'eat'))
p.put((3, 'sleep'))
while not p.empty():
    next_item = p.get()
    print(next_item)

#
# LISTS implemented as ARRAYS
#

list_ = [x for x in range(0, 10)]

# O(1) or O(n), Python lists are implemented as overallocated arrays
list_.append(10)
list_.append(20)
list_.append(30)

# O(1)
print(list_[5])

# O(1)
# gets last element
list_.pop()

# O(0), the whole array needs to be rewrited
list_.pop(0)

#
# DEQUE implemented as BIDIRECTIONAL LIST
#

from collections import deque
deque_ = deque()

# O(1), new element is allocated and only referenced in former last element
deque_.append('aaa')
deque_.append('bbb')
deque_.append('ccc')
deque_.append('ddd')
deque_.append('eee')

# O(n) - the whole list needs to be iterated
print(deque_[2])

# O(1) - list keeps references to both ends elements
deque_.pop()  # last element
deque_.popleft()  # first element

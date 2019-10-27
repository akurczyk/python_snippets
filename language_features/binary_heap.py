import heapq

h = []
h.append((5, 'aaa'))
h.append((10, 'bbb'))
h.append((2, 'ccc'))

heapq.heapify(h)

heapq.heappush(h, (8, 'ddd'))
heapq.heappush(h, (1, 'eee'))
heapq.heappush(h, (20, 'fff'))

while h:
    next_item = heapq.heappop(h)
    print(next_item)

import queue

q = queue.Queue()
print(q.empty())
q.put('bag1')
print(q.empty())
q.put('bag2')
q.put('bag3')
print(q.get())

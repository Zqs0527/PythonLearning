import queue

q = queue.Queue()
print(q.empty())
q.put('bag1')
print(q.empty())
q.put('bag2')
q.put('bag3')
print(q.get())


stack = list()
stack.append('bill1')
stack.append('bill2')
bill_type = stack.pop() # this will return 'bill2', because it is last in
print(bill_type)

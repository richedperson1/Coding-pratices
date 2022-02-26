from queue import Queue
 
q = Queue()

q.put('a')
q.put('b')
q.put('c')
lst = []
while q.empty()==False:
    lst.append(q.get())

while lst:
    q.put(lst[-1])
    lst.pop()

print(q.get())
print(q.get())
print(q.get())

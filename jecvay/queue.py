from collections import deque
#Pyhon list has enough function for queue
#but list is not too efficient

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft() #pop
queue.popleft()

print queue

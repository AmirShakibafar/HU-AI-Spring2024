from data_strctures.p_queue import PriorityQueue

p: PriorityQueue = PriorityQueue()

p.push("sag", 10)
p.push("sag2", 3)
p.push("sag3", 17)

print(p.pop())
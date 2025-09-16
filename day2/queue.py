from collections import deque

queue = deque([])

f = open("seq.txt")

for line in f:
    line = line.split()
    if line[0] == "insert":
        queue.append(line[1])
    elif line[0] == "remove":
        elem = queue.popleft()
        print("popped", elem)
    print(queue)
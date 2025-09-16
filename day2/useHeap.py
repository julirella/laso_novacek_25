import heapq

heap = []

f = open("seq.txt")

for line in f:
    input()
    line = line.split()
    if line[0] == "insert":
        heapq.heappush(heap, line[1])
    elif line[0] == "remove":
        elem = heapq.heappop(heap)
        print("popped", elem)
    print(heap)
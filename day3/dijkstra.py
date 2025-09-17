import math
import heapq

file = open("graphweighted.txt", 'r')

first_line = file.readline().split()
n = int(first_line[0])
m = int(first_line[1])

graph = [[] for _ in range(n)]

for i in range(m):
    line = file.readline().split()
    u = int(line[0])
    v = int(line[1])
    cost = int(line[2])
    graph[u].append((v, cost))
    graph[v].append((u, cost))

def dijkstra(s: int):
    dist = [math.inf] * n
    dist[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))

    while len(heap) > 0:
        _, node = heapq.heappop(heap)
        for neighbour, cost in graph[node]:
            if dist[neighbour] > dist[node] + cost:
                dist[neighbour] = dist[node] + cost
                heapq.heappush(heap, (cost + dist[node], neighbour))
                
    return dist

dist = dijkstra(0)
for i in range(n):
    if dist[i] == math.inf:
        print("unreachable")
    else:
        print(dist[i])

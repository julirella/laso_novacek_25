#source: https://cw.fel.cvut.cz/wiki/courses/laso/novacek
import math

file = open("graphweighted.txt", 'r')

first_line = file.readline().split()
n = int(first_line[0])
m = int(first_line[1])

edges = []
for i in range(m):
    line = file.readline().split()
    u = int(line[0])
    v = int(line[1])
    cost = int(line[2])
    edges.append((u, v, cost))
    edges.append((v, u, cost))

def dijkstra(s: int):
    dist = {s: 0}

    while True:
        min_edge = None
        min_score = math.inf
        for edge in edges:
            if edge[0] in dist \
                    and edge[1] not in dist \
                    and min_score > dist[edge[0]] + edge[2]:
                min_edge = edge
                min_score = dist[edge[0]] + edge[2]

        if not min_edge: break
        dist[min_edge[1]] = min_score
    return dist


dist = dijkstra(0)
for i in range(n):
    print(dist[i] if i in dist else "unreachable")

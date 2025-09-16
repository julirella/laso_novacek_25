from collections import deque
import math

def parse_line(line):
    nums = line.split()
    first = int(nums[0])
    second = int(nums[1])
    return first, second

def load_graph_list(path):
    f = open(path)
    nodes, edges = parse_line(f.readline())

    graph = [[] for _ in range(nodes)]

    for _ in range(edges):
        first, second = parse_line(f.readline())
        graph[first].append(second)
        graph[second].append(first)
    
    return graph

def bfs(graph, visited, dst, start):
    queue = deque([])
    queue.append(start)
    visited[start] = True
    dst[start] = 0

    while len(queue) > 0:
        parent = queue.popleft()
        neighbours = graph[parent]
        for n in neighbours:
            if visited[n] == False:
                visited[n] = True
                queue.append(n)
                dst[n] = dst[parent] + 1

graph = load_graph_list("graph.txt")

#bfs once
visited = [False] * len(graph)
dst = [math.inf] * len(graph) 

start = 0
bfs(graph, visited, dst, start)

#show visited nodes
print("Visited:",)
cnt = 0
for i in range(len(visited)):
    if visited[i] == True:
        print(i, end=", ")
        cnt += 1
print("\ntotal:", cnt, "out of", len(graph))

#show distance to node:
end = 7
print("Distance from", start, "to", end, ":", dst[end])

#count components:
visited = [False] * len(graph)
components = 0
for i in range(len(graph)):
    if visited[i] == False:
        bfs(graph, visited, dst, i)
        components += 1

print("components:", components)
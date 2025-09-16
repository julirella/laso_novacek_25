from sys import argv

def parse_line(line):
    line = line.strip()
    nums = line.split()
    first = int(nums[0])
    second = int(nums[1])
    return first, second

def load_graph_list(path):
    f = open(path)
    nodes, edges = parse_line(f.readline())

    print("nodes:", nodes, ", edges:", edges)

    graph = [[] for _ in range(nodes)]

    for _ in range(edges):
        first, second = parse_line(f.readline())
        graph[first].append(second)
        graph[second].append(first)
    
    return graph

def load_graph_dict(path):
    f = open(path)
    nodes, edges = parse_line(f.readline())
    
    graph = {}

    for _ in range(edges):
        first, second = parse_line(f.readline())
        
        if first in graph.keys():
            graph[first].append(second)
        else:
            graph[first] = [second]
        
        if second in graph.keys():
            graph[second].append(first)
        else:
            graph[second] = [first]
        
    return graph



def print_graph(graph):
    for i in range(len(graph)):
        print(i, ": ", graph[i])

path = argv[1]
graph = load_graph_list(path)
# graph = load_graph_dict(path)

print_graph(graph)
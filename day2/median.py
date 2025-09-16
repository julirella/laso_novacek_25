import heapq

class MedianHeap:
    def __init__(self) -> None:
        self.maxheap = []
        self.minheap = []

    def max_len(self):
        return len(self.maxheap)
    
    def min_len(self):
        return len(self.minheap)  

    def median(self):
        if  self.min_len() == self.max_len():
            if self.min_len == 0:
                return None
            else:
                return (min(self.minheap) - min(self.maxheap)) / 2
        elif self.min_len() > self.max_len():
            return min(self.minheap)
        else:
            return -min(self.maxheap)

    def insert(self, elem):
        if self.median() is None or elem > self.median():
            heapq.heappush(self.minheap, elem)
            if self.min_len() > self.max_len() + 1:
                tmp = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -tmp)
        else:
            heapq.heappush(self.maxheap, -elem)
            if self.max_len() > self.min_len() + 1:
                tmp = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -tmp)
            



f = open("seq.txt")

med_heap = MedianHeap()

for line in f:
    input()
    line = line.split()        
    if line[0] == "insert":
        med_heap.insert(int(line[1]))
    # elif line[0] == "remove":
    #     elem = med_heap.median()
    #     print("popped", elem)
    print(med_heap.minheap)
    print(med_heap.maxheap)
    print("median:", med_heap.median())
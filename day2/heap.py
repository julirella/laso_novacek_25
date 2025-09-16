#source: https://cw.fel.cvut.cz/wiki/courses/laso/novacek
import math

class Heap:
    def __init__(self):
        self.size = 0
        self.arr = []

    def insert(self, val:int):
        self.arr.append(val)
        self.size += 1
        self._bubble_up(self.size)

    def extract_min(self):
        self._swap(1, self.size)
        self.size -= 1
        self._bubble_down(1)
        return self.arr.pop(-1)

    def _bubble_up(self, i:int):
        if i is 1: return
        parentI:int = i//2
        if self.arr[i] < self.arr[parentI]:
            self._swap(i, parentI)
            self._bubble_up(parentI)

    def _bubble_down(self, i:int):
        left_child  = math.inf if i*2 > self.size else self.arr[i * 2]
        right_child = math.inf if i*2 + 1 > self.size else self.arr[i *2 + 1]

        smaller_child = None
        if(left_child < self.arr[i]):
            if(right_child < left_child):
                smaller_child = i * 2 + 1
            smaller_child = i*2
        elif right_child < self.arr[i]:
            smaller_child = i*2 + 1

        if smaller_child is not None:
            self._swap(i, smaller_child)
            self._bubble_down(smaller_child)

    def _swap(self, i:int, j:int):
        tmp:int = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = tmp



heap = Heap()

for line in open('seq.txt', 'r'):
    if(line.startswith('insert')):
        number = int(line.split()[1])
        heap.insert(number)
    else:
        print(heap.extract_min())


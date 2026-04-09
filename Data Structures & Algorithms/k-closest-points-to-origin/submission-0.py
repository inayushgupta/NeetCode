class MaxHeap:
    def __init__(self):
        self.data = []
        self.length = 0

    def insert(self, everything):
        value, element = everything

        self.data.append(everything)
        self.length += 1
        curr = self.length - 1

        while curr > 0 and self.data[(curr - 1)//2][0] < self.data[curr][0]:
            parent = (curr-1)//2
            self.data[parent], self.data[curr] = self.data[curr], self.data[parent]
            curr = parent
        
    def pop(self):
        self.data[0] = self.data[-1]
        self.length -= 1
        self.data.pop()

        curr = 0

        while True:

            smallest = curr

            left = curr * 2 + 1
            right = curr * 2 + 2

            if left < self.length and self.data[smallest][0] < self.data[left][0]:
                smallest = left
            
            if right < self.length and self.data[smallest][0] < self.data[right][0]:
                smallest = right
            
            if smallest == curr:
                break
            
            self.data[curr], self.data[smallest] = self.data[smallest], self.data[curr]

            curr = smallest
        
    def getheap(self):
        return self.data



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def give_distance(x, y):
            return math.sqrt((x) ** 2 + (y) ** 2)
                
        heap = MaxHeap()

        for point in points:
            x, y = point
            heap.insert([give_distance(x, y), point])
            if heap.length > k:
                heap.pop()
            
        return [x[1] for x in heap.getheap()]

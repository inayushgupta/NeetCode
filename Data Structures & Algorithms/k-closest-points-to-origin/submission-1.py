class Solution:
    def kClosest(self, points:List[List[int]], k:int) -> List[int]:

        heap = []

        for x,y in points:
            dist = -(x*x + y*y)
            heapq.heappush(heap, (dist, [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]
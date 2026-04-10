class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = [time for time in Counter(tasks).values()]
        queue  = collections.deque()
        heapq.heapify_max(counts)
        cycles = 0

        while counts or queue:
            cycles += 1
            if counts:
                task = heapq.heappop_max(counts) - 1
                if task:
                    queue.append([cycles+n, task])


            if queue:
                if queue[0][0] == cycles:
                    heapq.heappush_max(counts, queue.popleft()[1])

        return cycles
        
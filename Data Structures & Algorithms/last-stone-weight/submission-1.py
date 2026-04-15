class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            one, two = heapq.heappop_max(stones), heapq.heappop_max(stones)

            sub = abs(one-two)

            if sub:
                heapq.heappush_max(stones, sub)
        
        return stones[0] if len(stones) else 0

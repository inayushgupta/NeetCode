class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        min_speed = float("inf")

        while left <= right:
            mid = left + (right-left)//2
            total_time = self.timeTaken(piles, mid)

            if total_time > h:
                left = mid + 1
            elif total_time <= h:
                min_speed = min(min_speed, mid)
                right = mid - 1
                
        return min_speed
        

    def timeTaken(self, piles, k):
        time = 0

        for pile in piles:
            time += math.ceil(pile/k)
        
        return time

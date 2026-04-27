class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        if len(cost) <= 2:
            return min(cost)

        one, two = cost[1], cost[0]

        for i in range(2, len(cost)):
            one, two = cost[i] +  min(one, two), one
        
        return min(one, two)

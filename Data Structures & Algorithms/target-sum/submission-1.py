class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {0:1}

        for num in nums:

            new_dp = {}

            for s, w in dp.items():

                # for each existing sum we
                # add and sub and then save

                new_dp[s+num] = new_dp.get(s+num, 0) + w
                new_dp[s-num] = new_dp.get(s-num, 0) + w
            
            dp = new_dp

        return dp.get(target, 0)
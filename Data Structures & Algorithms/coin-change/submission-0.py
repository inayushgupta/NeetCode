class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        coins.sort()

        for total_amount in range(1, amount+1):

            for coin in coins:

                req = total_amount - coin
                if req < 0:
                    break
                
                dp[total_amount] = min(dp[req] + 1, dp[total_amount])

        return dp[-1] if dp[-1] != float('inf') else -1




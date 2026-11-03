class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        dp = [n for n in range(0, len(text2) + 1)]
        diag = 0

        for row in range(1, len(text1) + 1):
            
            diag = dp[0]
            dp[0] = row


            for col in range(1, len(text2) + 1):

                temp = dp[col]

                if text1[row-1] == text2[col-1]:
                    dp[col] = diag
                else:
                    dp[col] = min(dp[col], dp[col-1]) + 1
                
                diag = temp
            

        return (m + n - dp[n]) // 2
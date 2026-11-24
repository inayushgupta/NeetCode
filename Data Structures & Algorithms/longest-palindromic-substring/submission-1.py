class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        if n == 0:
            return ''

        dp = [[False] * n for _ in range(n)]

        longest = s[0]

        for i in range(n):
            dp[i][i] = True

        # checking 2 length strings
        for i in range(n-1):
            dp[i][i+1] = (s[i]==s[i+1])
            if dp[i][i+1]:
                longest = s[i:i+2]
            

        # for strings bigger than 2
        for length in range(3, n+1):

            for i in range(n-length+1):
                dp[i][i + length - 1] = (dp[i+1][i + length-2]) and (s[i] == s[i+length-1])      

                if dp[i][i+length-1]:
                    longest = s[i:i+length]   

        return longest
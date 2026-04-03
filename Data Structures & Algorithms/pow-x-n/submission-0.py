class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0000
        if n == 0:
            return ans
        elif n > 0:
            for _ in range(n):
                ans = ans * x
            return ans
        elif n < 0:
            for _ in range(abs(n)):
                ans = ans * x
            return (1.000/ans) 


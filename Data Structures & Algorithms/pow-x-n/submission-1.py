class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.00
        temp = self.myPow(x, abs(n)//2)
        res = temp*temp
        if n % 2 == 1: res = res * x
        if n < 0: return 1.00/res
        return res

        


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        point = 0
        if len(s) > len(t):
            return False
        for c in t:
            if point < len(s) and s[point] == c:
                point+=1
                
        return point == len(s)
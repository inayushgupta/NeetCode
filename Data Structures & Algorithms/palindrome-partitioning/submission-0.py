class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []

        def helper(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    part.append(s[i:j+1])
                    helper(j+1)
                    part.pop()
        
        helper(0)
        return res
        
    def isPal(self, string, i, j):
    
        while i <= j:
            if string[i] != string[j]:
                return False
            i, j = i+1, j-1
        return True
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s2):
            return False
        
        perm = {}
        s_one = Counter(s1)
        size = len(s1)

        for i in range(len(s2)):
            s_two = Counter(s2[i:i+size])

            if s_one == s_two:
                return True
            
        
        return False



        
        return True 


        
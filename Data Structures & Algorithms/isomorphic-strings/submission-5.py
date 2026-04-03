class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s)-len(t):
            return False
        
        mapping = {}
        used_t = set()

        for i in range(len(s)):
            cs, ct = s[i], t[i]

            if cs in mapping:
                if mapping[cs] != ct:
                    return False
            else:
                if ct in used_t:
                    return False
                mapping[cs] = ct
                used_t.add(ct)
        return True


        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        required = Counter(t)
        wanted = len(required)
        have = {}
        got = 0
        left = 0
        smallest = ""

        for right in range(len(s)):

            char = s[right]            
            have[char] = have.get(char, 0) + 1


            if char in required and required[char] == have[char]:
                got += 1
            
            while got == wanted:
                # substring is valid
                if not smallest or (right - left + 1) < len(smallest):
                    smallest = s[left:right+1]
                
                # here we will shink
                char_left = s[left]

                if char_left in required and required[char_left] == have[char_left]:
                    got -= 1
                
                have[char_left] -= 1
                left += 1
        
        return smallest




        
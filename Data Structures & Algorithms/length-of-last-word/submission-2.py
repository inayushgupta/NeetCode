class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        longest = 0
        length = 0
        last = ""
        for c in s:
            if c == " ":
                last = c
            else:
                if last == "" or last == " ":
                    length = 0
                length+=1
                longest = length
            last = c
        return longest

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        last = ""
        for c in s:
            if c == " ":
                last = c
            else:
                if last == "" or last == " ":
                    length = 0
                length+=1
            last = c
        return length

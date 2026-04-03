class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i, c in enumerate(s):
            if i == 0:
                continue
            score = score + abs(ord(s[i-1]) - ord(c))
        return score
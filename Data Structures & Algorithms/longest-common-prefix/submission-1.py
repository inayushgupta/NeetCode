class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if not strs: return ""
        for s in strs:
            if len(s) > len(prefix):
                s = s[:len(prefix)]
            else:
                prefix = prefix[:len(s)]

            for i, c in enumerate(s):
                if c != prefix[i]:
                    prefix = prefix[:i]
                    break
        return prefix
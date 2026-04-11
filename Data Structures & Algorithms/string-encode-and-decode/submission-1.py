class Solution:

    def encode(self, strs: List[str]) -> str:
        concat = ""
        for s in strs:
            concat += f'{len(s)}#{s}'
        return concat

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            j += 1
            strs.append(s[j:j+length])
            i = j + length

        return strs
        
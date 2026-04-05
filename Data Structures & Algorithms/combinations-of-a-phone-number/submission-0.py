class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        # const
        length = len(digits)

        res = []
        intermediate = []

        def backtrack(i):

            if i == length:
                res.append(''.join(intermediate))
                return

            letters = phone_map[digits[i]]

            for letter in letters:

                intermediate.append(letter)
                backtrack(i+1)
                intermediate.pop()

        backtrack(0)

        return res
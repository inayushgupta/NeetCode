class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for r in board:
            seen = set()
            for c in r:
                if c == ".": continue
                if c in seen: return False
                seen.add(c)
        
        # column check
        for c in range(9):
            seen = set()
            for r in range(9):
                num = board[r][c]
                if num == ".": continue
                if num in seen: return False
                seen.add(num)

        # box check
        for r1 in range(0, 9, 3):
            for c1 in range(0, 9, 3):
                seen = set()
                for r2 in range(r1, r1+3):
                    for c2 in range(c1, c1+3):
                        num = board[r2][c2]
                        if num == ".": continue
                        if num in seen: return False
                        seen.add(num)

        return True

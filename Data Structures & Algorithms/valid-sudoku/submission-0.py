class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        for r in board:
            elements = set()
            for c in r:
                if c == ".": continue
                if c in elements: return False
                elements.add(c)
        
        #col check
        row, col = 9, 9
        for c in range(col):
            elements = set()
            for r in range(row):
                num = board[r][c]
                if num == ".": continue
                if num in elements: return False
                elements.add(num)

        #box check
        for r1 in range(0, 9, 3):
            for c1 in range(0, 9, 3):
                elements = set()
                for r2 in range(r1, r1+3, 1):
                    for c2 in range(c1, c1+3, 1):
                        num = board[r2][c2]
                        if num == ".": continue
                        if num in elements: return False
                        elements.add(num)

        return True
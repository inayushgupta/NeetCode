class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = [-1] * n
        res = []

        def out_gen():
            board = [] 
            for i in range(n):
                board.append("." * (cols[i]) + "Q" + "." * (n - 1 -cols[i]))
            return board
        
        def isSafe(row, col):
            for i in range(row):
                if cols[i] == col:
                    return False
                if abs(cols[i] - col) == abs(row - i):
                    return False
            return True
        
        def helper(row_num):
            if row_num == n:
                res.append(out_gen())
                return
            
            for col in range(n):
                if isSafe(row_num, col):
                    cols[row_num] = col
                    helper(row_num + 1)
                    cols[row_num] -= 1
            
        helper(0)
        return res

            
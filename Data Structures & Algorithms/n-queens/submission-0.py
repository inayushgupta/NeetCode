class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = [-1] * n
        res = []

        # output converter
        def out_give():
            board = []
            for i in range(n):
                board.append(
                    ( "." * (cols[i]) ) + "Q" +  ( '.' * ( n - 1 - cols[i]) )
                )
            return board
        
        def isSafe(row, col):

            for i in range(row):
                # column check
                if cols[i] == col:
                    return False
                if abs(cols[i] - col) == abs(row - i):
                    return False
            return True

        def helper(rownum):

            if rownum == n:
                res.append(out_give())
                return

            for col in range(n):
                if isSafe(rownum, col):
                    cols[rownum] = col
                    helper(rownum + 1)
                    cols[rownum] -= 1
        
        helper(0)
        return res










class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = 0
        diag = 0
        adiag = 0
        count = 0
        diagt = 2*(n) - 1

        def backtracking(row_index):
            nonlocal count, cols, diag, adiag

            if row_index == n:
                count += 1
                return

            # check if it can be placed in this place or not
            # for the queen to be placed it must satisfy
            # anti-diag, diag, and cols free

            for col_index in range(n):

                diag_no = (row_index - col_index) + (n - 1)
                anti_diag_no = row_index + col_index

                col_possible = cols & (1 << (n - col_index))
                diag_possible = diag & (1 << (diagt - diag_no))
                anti_possible = adiag & (1 << (diagt - anti_diag_no))

                if not(col_possible or diag_possible or anti_possible):
                    
                    # setting variables
                    cols |= 1 << (n-col_index)
                    diag |= 1 << (diagt - diag_no)
                    adiag |= 1 << (diagt - anti_diag_no)

                    backtracking(row_index+1)

                    # resetting variables
                    cols &= ~(1 << (n-col_index))
                    diag &= ~(1 << (diagt - diag_no))
                    adiag &= ~(1 << (diagt - anti_diag_no))

                else:
                    continue

        backtracking(0)
        return count
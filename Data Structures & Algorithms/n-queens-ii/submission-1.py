class Solution:
    def totalNQueens(self, n: int) -> int:

        cols, diag, adiag = 0, 0, 0
        count = 0

        def backtracking(row_index):
            nonlocal count, cols, diag, adiag

            if row_index == n:
                count += 1
                return

            for col_index in range(n):

                diag_no = (row_index - col_index) + (n - 1)
                anti_diag_no = row_index + col_index

                col_possible = cols & (1 << col_index)
                diag_possible = diag & (1 <<  diag_no)
                anti_possible = adiag & (1 << anti_diag_no)

                if not (col_possible or diag_possible or anti_possible):
                    
                    # setting variables
                    cols |= 1 << col_index
                    diag |= 1 << diag_no
                    adiag |= 1 << anti_diag_no

                    backtracking(row_index+1)

                    # resetting variables
                    cols &= ~(1 << col_index)
                    diag &= ~(1 << diag_no)
                    adiag &= ~(1 << anti_diag_no)

                else:
                    continue

        backtracking(0)
        return count
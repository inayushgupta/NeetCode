class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        if len(word) > rows * cols:
            return False
        
        index = 0

        def helper(row, col) -> bool:
            nonlocal index

            if index == len(word):
                return True

            if row >= rows or row < 0 or col >= cols or col < 0:
                return False
            
            letter = board[row][col]

            if letter == '!':
                return False
            
            if letter != word[index]:
                return False

            board[row][col] = '!'
            index += 1

            result = (
                helper(row + 1, col)
                or helper(row - 1, col)
                or helper(row, col + 1)
                or helper(row, col - 1)
            )

            index -= 1
            board[row][col] = letter
            return result


        for row_num in range(rows):
            for col_num in range(cols):

                curr_letter = board[row_num][col_num]
                if curr_letter == word[0]:
                    if helper(row_num, col_num):
                        return True
        
        return False
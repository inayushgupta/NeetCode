class Solution:

    def whereami(self, row, col):

        # check for the maximum longest path
        # if any of the direction goes out of bound
        # just ignore that direciton
        # only take the direction where the the matrix[row][col] is smaller
        # than the current position
        # and when the directions are final
        # only then take the maximum and add one to it and store
        # if none of the direction is possible than just put 1 and move on

        if self.dp[row][col] != -1:
            return self.dp[row][col]

        possible_ways = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for rx, cx in directions:
            nr, nc = row+rx, col+cx

            if not (nr < 0 or nr >= self.m or nc < 0 or nc >= self.n):
                if self.matrix[nr][nc] < self.matrix[row][col]:
                    possible_ways.append(self.whereami(nr, nc))

        self.dp[row][col] = max(possible_ways, default=0) + 1

        return self.dp[row][col]

        

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])

        self.dp = [[-1] * self.n for _ in range(self.m)]

        for row in range(self.m):
            for col in range(self.n):

                if self.dp[row][col] == -1:
                    self.whereami(row, col)

        longest = float('-inf')

        for row in self.dp:
            longest = max(longest, max(row))
        
        return longest
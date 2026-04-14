class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0

        def helper(r, c, curr_area):
            nonlocal max_area
            
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0 

            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            curr_area = curr_area + 1 + ( helper(r+1, c, curr_area)
            + helper(r-1, c, curr_area)
            + helper(r, c+1, curr_area)
            + helper(r, c-1, curr_area))

            max_area = max(max_area, curr_area)

            return curr_area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    helper(i, j, 0)
        return max_area
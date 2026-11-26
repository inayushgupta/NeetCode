class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxarea = 0
        heights = heights + [0]
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                new_height = heights[stack.pop()]
                new_width = i - (stack[-1] if stack else -1) - 1
                maxarea = max(maxarea, new_height * new_width)
            stack.append(i)
        return maxarea
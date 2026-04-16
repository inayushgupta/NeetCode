# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            return_value = max(node.val, node.val + left, node.val + right)

            max_sum = max(return_value, max_sum, left + node.val + right)

            return return_value

        dfs(root)

        return max_sum
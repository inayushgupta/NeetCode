# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: return True 
        if not root: return False

        def dfs(node):
            if not node: return False

            if self.check(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        


    def check(self, root1, root2) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False

        if root1.val != root2.val : return False

        return (
            self.check(root1.left, root2.left) and 
            self.check(root1.right, root2.right)
        )










            
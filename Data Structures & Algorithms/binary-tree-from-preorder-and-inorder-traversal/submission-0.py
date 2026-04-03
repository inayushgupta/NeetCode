# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        value_to_index = {x:y for y, x in enumerate(inorder)}

        def builder(index, left, right):

            if left > right:
                return None

            rootval = preorder[index]
            newnode = TreeNode(rootval)
            inorderindex = value_to_index[rootval]
            left_size = inorderindex - left

            newnode.left = builder(index + 1, left, inorderindex-1)
            newnode.right = builder(index + 1 + left_size, inorderindex+1, right)

            return newnode

        return builder(0, 0, len(preorder)-1)



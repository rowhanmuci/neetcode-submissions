# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def maxdepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = maxdepth(node.left)
            right = maxdepth(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)
            
        maxdepth(root)
        return self.max_diameter
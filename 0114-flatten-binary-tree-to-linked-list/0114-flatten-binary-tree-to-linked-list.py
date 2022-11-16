# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        
        self.flatten(root.right)
        self.flatten(root.left)
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        
        leave = root
        while leave.right:
            leave = leave.right
        
        leave.right = right
        
        
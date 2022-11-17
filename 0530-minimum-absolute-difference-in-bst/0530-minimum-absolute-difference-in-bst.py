# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.diff = 100000000
        self.prev = None
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.diff
    
    def dfs(self, root):
        if not root:
            return
        
        self.dfs(root.left)
        if self.prev is not None:
            self.diff = min(self.diff, root.val - self.prev)
        self.prev = root.val
        self.dfs(root.right)  
        
        
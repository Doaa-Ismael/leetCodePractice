# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        self.curCount = 1
        self.ans = []
        self.maxCount = -10000000
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root)
        return self.ans
    
         
    def helper(self, root):
        if not root: 
            return
        
        self.helper(root.left)
        
        self.curCount = self.curCount + 1 if root.val == self.prev else 1
        
        if self.maxCount == self.curCount:
            self.ans.append(root.val)
        
        if self.maxCount < self.curCount:
            self.maxCount = self.curCount
            self.ans = [root.val]

        self.prev = root.val  
        self.helper(root.right)

    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        self.countNumbers(root, count)
        modeVal = max(count.values())
        return [num for (num, c) in count.items() if c == modeVal]
    
        
        
        
    def countNumbers(self, root: Optional[TreeNode], count):
        if not root:
            return
        
        count[root.val] = count.get(root.val, 0) + 1
        self.countNumbers(root.left, count)
        self.countNumbers(root.right, count)
        
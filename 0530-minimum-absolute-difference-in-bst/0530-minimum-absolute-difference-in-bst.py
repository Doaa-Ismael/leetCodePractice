# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorderdfs = []
        self.helper(root, inorderdfs)
        ans = 10000000
        for i in range(0, len(inorderdfs) - 1 ):
            ans = min(ans,abs(inorderdfs[i] - inorderdfs[i+1]))
            
        return ans
        
        
    def helper(self, root, inorderdfs):
        if not root:
            return
        self.helper(root.left, inorderdfs)
        inorderdfs.append(root.val)
        self.helper(root.right, inorderdfs)

        
        
        
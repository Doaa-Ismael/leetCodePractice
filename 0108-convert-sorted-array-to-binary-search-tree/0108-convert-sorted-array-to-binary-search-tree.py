# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        rootParent = TreeNode(-1000000)
        self.recursivelyBuildBTS(nums, rootParent, 0, len(nums) - 1)
        return (rootParent.left or rootParent.right)
        
        
    def recursivelyBuildBTS(self, nums, root, l, r):
        if l > r:
            return
        
        mid = l + (r-l) // 2
        val = nums[mid]
        newNode = TreeNode(val)
        if root.val < val:
            root.right = newNode
        else:
            root.left = newNode

        self.recursivelyBuildBTS(nums, newNode, l, mid-1)
        self.recursivelyBuildBTS(nums, newNode, mid+1, r)
        
        
        
        
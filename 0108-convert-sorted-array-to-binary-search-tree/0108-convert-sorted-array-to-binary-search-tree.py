# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.recursivelyBuildBTS(nums, 0, len(nums) - 1)
        
        
    def recursivelyBuildBTS(self, nums, l, r):
        if l > r:
            return
        
        mid = l + (r-l) // 2
        newNode = TreeNode(nums[mid])

        newNode.left = self.recursivelyBuildBTS(nums, l, mid-1)
        newNode.right = self.recursivelyBuildBTS(nums, mid+1, r)
        
        return newNode
        
        
        
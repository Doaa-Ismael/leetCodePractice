# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return 
        
        preorder = []
        self.preordertraverse(root, preorder)
        n = len(preorder)
        for i in range(0, n - 1):
            preorder[i].right = preorder[i+1]
            preorder[i].left = None
        
        return preorder[0]
        
        
    
    def preordertraverse(self, root: Optional[TreeNode], preorder: List[TreeNode]) -> None:
        
        if not root: return
        
        preorder.append(root)
        self.preordertraverse(root.left, preorder)
        self.preordertraverse(root.right, preorder)

        
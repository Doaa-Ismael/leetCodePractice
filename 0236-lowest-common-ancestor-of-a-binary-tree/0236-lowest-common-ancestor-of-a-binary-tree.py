# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # 1) find the ancesstors of the two nodes and sort them and find the lowest one
        #  find children of every node and if it contans p and q I will add it to the list
        # find children of each node and if it has all 
        
        preorder1 = []
        preorder2 = []
        self.preorder(root, preorder1, p.val)
        self.preorder(root, preorder2, q.val)
        print([v.val for v in preorder1])
        print([v.val for v in preorder2])
        
        
        for a1 in preorder1:
            for a2 in preorder2:
                if a1.val == a2.val:
                    return a1    
        
        
    def preorder(self, root, preorderList, n) -> None:
        if not root:
            return        
        
        if root.val == n:
            preorderList.append(root)
            return True
        if self.preorder(root.left, preorderList, n):
            preorderList.append(root)
            return True
            
        if self.preorder(root.right, preorderList, n):
            preorderList.append(root)  
            return True
        
        
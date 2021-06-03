# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        successor = None
        
        while root:
            if p.val >= root.val:
                # skip the left subtree and root
                root = root.right
            else:
                # p.val < root.val
                # result could be in left subtree or the root itself
                successor = root
                root = root.left
        
        return successor

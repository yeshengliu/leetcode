# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        lowest = root
        
        def helper(node):
            if not node:
                return False
            
            left = helper(node.left)
            right = helper(node.right)
            
            # If node is p or q
            mid = node == p or node == q
            
            if mid + left + right == 2:
                nonlocal lowest
                lowest = node
            
            return mid or left or right
        
        helper(root)
        
        return lowest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.is_uni(root)
        return self.count
        
    # Check whether subtree is uni-value
    def is_uni(self, node):
        if not node:
            return True
        
        # Node has no children
        if node.left is None and node.right is None:
            self.count += 1
            return True
        
        # Check if all chidren are univalue subtrees
        is_uni = True
        
        if node.left:
            is_uni = self.is_uni(node.left) and is_uni and node.val == node.left.val
        
        if node.right:
            is_uni = self.is_uni(node.right) and is_uni and node.val == node.right.val       
        # If all children are univalue subtrees, increment count
        if is_uni:
            self.count += 1
        
        return is_uni

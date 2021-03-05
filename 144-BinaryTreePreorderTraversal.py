# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self.preorderTraversalHelper(values, root)
        return values
    
    def preorderTraversalHelper(self, values, node):
        if not node:
            return
        # Append root
        values.append(node.val)
        # Append left child
        self.preorderTraversalHelper(values, node.left)
        # Append right child
        self.preorderTraversalHelper(values, node.right)

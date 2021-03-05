# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self.inorderTraversalHelper(values, root)
        return values
    
    def inorderTraversalHelper(self, values, node):
        if not node:
            return
        # Inorder Traversal
        # Traverse left subtree first
        # then root
        # then traverse right subtree
        self.inorderTraversalHelper(values, node.left)
        values.append(node.val)
        self.inorderTraversalHelper(values, node.right)

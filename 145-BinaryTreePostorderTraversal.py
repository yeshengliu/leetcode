# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self.postorderTraversalHelp(values, root)
        return values
    
    def postorderTraversalHelp(self, values, node):
        if not node:
            return
        # Traverse left subtree first
        # then traverse right subtree
        # then add the root
        self.postorderTraversalHelp(values, node.left)
        self.postorderTraversalHelp(values, node.right)
        values.append(node.val)

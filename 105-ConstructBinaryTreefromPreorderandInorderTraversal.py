# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not(preorder and inorder):
            return None
        
        # preorder: root, left, right
        # inorder: left, root, right
        curr_value = preorder.pop(0)
        idx = inorder.index(curr_value)
        
        left = self.buildTree(preorder, inorder[:idx])
        right = self.buildTree(preorder, inorder[idx+1:])
        return TreeNode(curr_value, left, right)
        

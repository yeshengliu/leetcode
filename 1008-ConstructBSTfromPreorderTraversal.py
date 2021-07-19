# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        for nodeValue in preorder[1:]:
            node, child = stack[-1], TreeNode(nodeValue)
            
            # find the parent node
            while stack and stack[-1].val < child.val:
                node = stack.pop()
            
            if child.val > node.val:
                node.right = child
            else:
                node.left = child
            
            stack.append(child)
        
        return root
        
        

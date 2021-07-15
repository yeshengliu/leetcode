# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # Do an in-order traversal and verify if current output
        # is larger than the previous output
        
        # in-order: left -> parent -> right
        
        stack = []
        curr = root
        prev = None
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            # Verify if current output is larger than previous output
            curr = stack.pop()
            if prev is not None and prev >= curr.val:
                return False
            prev = curr.val
            
            # continue traversing
            curr = curr.right
        
        return True
            
            

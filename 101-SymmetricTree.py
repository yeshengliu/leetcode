# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        # Given two node, compare if they are symmetric
        def isSymmetricHelper(nodeX, nodeY):
            # Both nodeX and nodeY is None
            if not(nodeX or nodeY):
                return True
            # Only one of nodeX and nodeY is None
            if (not nodeX) or (not nodeY):
                return False
            # NodeX and NodeY have different values
            if nodeX.val != nodeY.val:
                return False
            # Compare childs
            b1 = isSymmetricHelper(nodeX.left, nodeY.right)
            b2 = isSymmetricHelper(nodeX.right, nodeY.left)
            return b1 and b2
        
        return isSymmetricHelper(root.left, root.right)

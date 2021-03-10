# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        values = []
        
        if not root:
            return values
        
        def levelOrderHelper(node, level):
            if node:
                # Add the new level to output if not exists
                if len(values) == level:
                    values.append([])
                # Add the current node value
                values[level].append(node.val)
                # Traverse left and right
                levelOrderHelper(node.left, level + 1)
                levelOrderHelper(node.right, level + 1)
        
        levelOrderHelper(root, 0)
        return values

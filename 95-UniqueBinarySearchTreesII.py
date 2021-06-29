# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def generate_trees(start, end):
            if start > end:
                return [None]
            results = []
            
            for i in range(start, end + 1):
                # all left subtrees if i is root
                left_trees = generate_trees(start, i - 1)
                
                # all right subtrees if i is root
                right_trees = generate_trees(i + 1, end)
                
                # connect left and right subtrees to root i
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        results.append(root)
                
            return results
            
        return generate_trees(1, n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def connectHelper(node):
            if not node:
                return
            if node.left:
                node.left.next = node.right
            if node.right:
                if node.next:
                    node.right.next = node.next.left
                else:
                    node.right.next = None
            
            connectHelper(node.left)
            connectHelper(node.right)
        
        connectHelper(root)
        return root
        

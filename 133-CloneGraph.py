"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def __init__(self):
        # mapping from original node to cloned node
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # return None if node is None
        if not node:
            return None
    
        # Return the mapped cloned node if it is already cloned
        if node in self.visited:
            return self.visited[node]
        
        # Clone the node
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        
        # Clone all neighbors
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        return clone_node
        
        

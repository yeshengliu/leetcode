"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None
        
        # Deep copy the new list
        # Keep track mapping old node -> new node
        # Instead of creating a mapping table, we can insert new node
        # between old nodes
        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next, None)
            curr = curr.next.next
        
        # Add random pointers
        curr = head
        while curr and curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next
        
        # Take new nodes out of link with old nodes
        new_head = head.next
        curr = new_head
        while curr.next:
            curr.next = curr.next.next
            curr = curr.next
        
        return new_head
        
        

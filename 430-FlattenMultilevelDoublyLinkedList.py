"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        curr = head
        
        # Traverse the list
        while curr:
            rest = curr.next
            
            if curr.child:
                # Flat the child list and connect to curr
                curr.next = self.flatten(curr.child)
                curr.next.prev = curr
                
                curr.child = None
                
                # Traverse to the last node of child
                while curr.next:
                    curr = curr.next
            
            # connect curr to the rest of list
            if rest:
                curr.next = rest
                rest.prev = curr
            
            curr = curr.next
        
        return head
                
        
        
        

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # Insert directly to head if head is null
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head
        
        # Use two pointers to justify where to insert the value
        prev = head
        curr = head.next
        
        toInsert = False
        
        while curr:
            # Case 1: insert if insertVal is in between of two adjacent
            # node values
            if prev.val <= insertVal and insertVal <= curr.val:
                toInsert = True
            # Case 2: insert if prev.val > curr.val, which means insertVal can be
            # the min or max of the list
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                return head
            
            prev, curr = prev.next, curr.next
            # Case 3: does not fall in first two cases and prev reached 
            # the begining of the list, which means all values are uniform
            if prev == head:
                break
            
        # Insert at the end if list only contain 1 value
        prev.next = Node(insertVal, curr)
        return head
                
                
            
        

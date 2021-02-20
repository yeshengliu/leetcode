# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # Create a new node ahead of head so we don't need
        # a special case to handle head.val
        
        sentinel = ListNode(0, head)
        
        prev = sentinel
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return sentinel.next
            

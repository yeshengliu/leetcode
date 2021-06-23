# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        
        prevHead = head
        
        while prevHead.next:
            curr = prevHead.next
            # move curr to the head
            prevHead.next = curr.next
            curr.next = head
            head = curr
        
        return head

# Recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        left = self.reverseList(head.next)
        # Place head node at the end
        head.next.next = head
        head.next = None
        
        return left         

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Return head if head is None
        if not head:
            return head
        
        # Return original list if k = 0
        if k == 0:
            return head
        
        # Observe that no matter how large k is, the actual 
        # num of rotation we need to perform is k mod length
        tail = head
        length = 1
        
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        
        if k == 0:
            return head
        
        # Go to the future last node of the new list
        last = head
        for _ in range(length - k - 1):
            last = last.next
        
        # Adjust pointers
        new_head = last.next
        tail.next = head
        last.next = None
        
        return new_head
            
        

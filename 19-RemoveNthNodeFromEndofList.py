# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Make two pointers, the distance between them should be n + 1
        when pointerB reach the end (None), delete the node
        next to pointerA
        """
        pointerA = pointerB = head
        
        for _ in range(n+1):
            if not pointerB:
                # pointerB already reached the end, which means head should be removed
                head = head.next
                return head
            pointerB = pointerB.next
        
        while pointerB:
            pointerA = pointerA.next
            pointerB = pointerB.next
        
        pointerA.next = pointerA.next.next
        
        return head

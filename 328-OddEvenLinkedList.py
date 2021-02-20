# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        # Empty list
        if not head:
            return head
        
        # 2nd node will be the head of even nodes section
        oddHead = head
        evenHead = head.next
        
        # Adjust next pointers
        odd = oddHead
        even = evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenHead
        
        return head
        

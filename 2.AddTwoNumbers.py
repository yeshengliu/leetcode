# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = curr = ListNode()
        carry = 0
        
        while l1 or l2 or carry:
            v1 = v2 = 0
            
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, digit = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next
        
        return output.next
        
            
        

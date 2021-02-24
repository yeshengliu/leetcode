# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # 1) Find where the first half is ended
        # 2) Reverse the second half
        # 3) Compare first and second half, if there
        #   is diff, return false
        
        # Find length
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next
        
        if length <= 1:
            return True
        
        # Find the node where second half begins
        second_head = head
        for i in range(length // 2):
            second_head = second_head.next
        
        # Reverse the second half
        prev_second_head = second_head
        while prev_second_head.next != None:
            curr = prev_second_head.next
            prev_second_head.next = curr.next
            curr.next = second_head
            second_head = curr
        
        # Compare first and second half
        first = head
        second = second_head
        while first != second_head and second != None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
        
        

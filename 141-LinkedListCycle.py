# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Turtle and Hare Algorithm
        if head == None:
            return False
        walk = head
        run = head.next
        while walk != run:
            if run == None or run.next == None:
                return False
            walk = walk.next
            run = run.next.next
        return True

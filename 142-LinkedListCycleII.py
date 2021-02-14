# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Phase 1: Use tortoise and Hare algorithm to identify
        if there exists a cycle
        """
        walk = head
        run = head
        while True:
            if run == None or run.next == None or run.next.next == None:
                return None
            walk = walk.next
            run = run.next.next
            if walk == run:
                break
        intersection = walk
        
        """
        Phase 2: Now we have the node where pointers meet together
        
        Suppose the distance from head to where cycle begins is x,
        distance from where cycle begins to intersection is y,
        distance for remaining cycle is z
        then 2 * (x + y) = x + y + N * (y + z)
            => x + y = N * (y + z)
            => x = (N - 1) * (y + z) + z
        which means, if we put walk pointer at head again, and another walk
        pointer at the intersection
        
        At the time they meet each other, the new intersection will be the node
        where cycle begins
        """
        pointerA = head
        pointerB = intersection
        while pointerA != pointerB:
            pointerA = pointerA.next
            pointerB = pointerB.next
        return pointerA
        

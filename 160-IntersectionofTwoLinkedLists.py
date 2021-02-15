# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Assume there is an intersection, the distance between
        headA to intersection is m1, headB to intersection is m2, 
        the rest distance is n
        Make the first pointer start at headA, and second pointer start at headB,
        and move one node at a time
        After reaching to the end, continue from the head of the other linked list
        At the time they meet each other, they should both travel m1 + m2 + n nodes
        If there is no intersection, they will not meet each other
        """
        
        if headA == None or headB == None:
            return None
        
        pointerA = headA
        pointerB = headB
        
        while pointerA != pointerB:
            pointerA = headB if pointerA == None else pointerA.next
            pointerB = headA if pointerB == None else pointerB.next
        
        # if there is no intersection, pointerA == pointerB == None
        
        return pointerA
            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        def swap(node):
            if not node or not node.next:
                return node
            
            node_next = node.next
            node.next = node_next.next
            node_next.next = node
            node.next = swap(node.next)
            return node_next
        
        return swap(head)

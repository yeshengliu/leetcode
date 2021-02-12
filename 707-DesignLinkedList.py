class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0, None)    # Sentinel
        self.length = 0            # Linked list length
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        curr = self.head
        while index >= 0:
            curr = curr.next
            index -= 1
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head.next = ListNode(val, self.head.next)
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = ListNode(val, None)
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.length:
            return
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1
        curr.next = ListNode(val, curr.next)
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1
        curr.next = curr.next.next
        self.length -= 1

class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

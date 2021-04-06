class Node:
    def __init__(self, val):
        self.val = val
        self.min = None
        self.next = None

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, val: int) -> None:
        insert = Node(val)
        if not self.head:
            insert.min = val
            self.head = insert
        else:
            insert.min = min(val, self.head.min)
            insert.next = self.head
            self.head = insert

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        if self.head:
            return self.head.val

    def getMin(self) -> int:
        if self.head:
            return self.head.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # q1 stores the data in the same order as stack
        # q2 is the helper queue when adding new item
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # Move all items from q1 to q2
        while self.q1:
            self.q2.append(self.q1.pop(0))
        # Push the new item to q1
        self.q1.append(x)
        # Move all items from q2 back to q1
        while self.q2:
            self.q1.append(self.q2.pop(0))
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # Remove the first item from q1
        if self.q1:
            return self.q1.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

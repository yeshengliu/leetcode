class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # s1 stores items in the queue, s2 is a helper stack for pushing new item
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # Move elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        # Append the new item at the bottom of s1
        self.s1.append(x)
        # Move elements from s2 back to s1
        while self.s2:
            self.s1.append(self.s2.pop())
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # Delete element from s1
        if self.s1:
            return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s1:
            return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

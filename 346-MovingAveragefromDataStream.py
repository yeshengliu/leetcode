class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = size
        self.total = 0
        

    def next(self, val: int) -> float:
        newNode = ListNode(val)
        
        if not self.head:
            self.size += 1
            self.head = newNode
            self.tail = newNode
        else:
            if self.size < self.capacity:
                self.size += 1
            else:
                # Remove head node if capacity is full
                self.total -= self.head.val
                self.head = self.head.next
            self.tail.next = newNode
            self.tail = newNode
        
        self.total += val
        
        return self.total * 1.0 / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

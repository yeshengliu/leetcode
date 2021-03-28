class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.size = 0
        self.head = 0
        self.tail = k - 1

    def enQueue(self, value: int) -> bool:
        # Insert an element into the circular queue
        # Return false if the queue is full
        if self.size == self.capacity:
            return False
        # move the last pointer
        if self.tail != self.capacity - 1:
            self.tail += 1
        else:
            self.tail = 0
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # Delete an element from the circular queue
        # Return false if the queue is empty
        if self.isEmpty():
            return False
        # move the front pointer
        if self.head != self.capacity - 1:
            self.head += 1
        else:
            # Move to the beginning
            self.head = 0
        self.size -= 1
        return True

    def Front(self) -> int:
        # Get the front item from the queue
        # If the queue is empty, return -1
        if self.size == 0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        # Get the last item from the queue
        # If the queue is empty, return -1
        if self.size == 0:
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

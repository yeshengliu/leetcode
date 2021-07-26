class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.mostRecent = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # move the node to the head of mostRecent list
            self.mostRecent.remove(node)
            self.mostRecent.addToHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.mostRecent.remove(node)
            self.mostRecent.addToHead(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self.mostRecent.addToHead(node)
        self.size += 1
        
        if self.size > self.capacity:
            # remove the least used node
            leastUsedNode = self.mostRecent.getLeastUsedNode()
            self.cache.pop(leastUsedNode.key)
            self.mostRecent.remove(leastUsedNode)
            self.size -= 1
        
class DoublyLinkedList:
    def __init__(self):
        # head & tail dummy nodes
        self.head = Node(None, 0)
        self.tail = Node(None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def getLeastUsedNode(self):
        if self.tail.prev.key is None:
            return None
        return self.tail.prev
        
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

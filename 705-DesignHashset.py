class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.NUM_BRACKETS = 1000
        self.arr = [[] for _ in range(self.NUM_BRACKETS)]

    def add(self, key: int) -> None:
        # compute hash
        h = key % self.NUM_BRACKETS
        # add the key into arr, first identify whether the item is already
        # in the set
        for item in self.arr[h]:
            if item == key:
                return
        self.arr[h].append(key)

    def remove(self, key: int) -> None:
        # compute hash
        h = key % self.NUM_BRACKETS
        # remove the key from arr
        if key in self.arr[h]:
            self.arr[h].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        # compute hash
        h = key % self.NUM_BRACKETS
        # loop the array
        for item in self.arr[h]:
            if item == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.CAPACITY = 1000
        self.keySet = [[] for _ in range(self.CAPACITY)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # compute hash
        h = key % self.CAPACITY
        # check the self.keySet
        # if key not exists, insert the key-value pair
        # if key exists, update value
        for pair in self.keySet[h]:
            if pair[0] == key:
                pair[1] = value
                return
        self.keySet[h].append([key, value])
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # compute hash
        h = key % self.CAPACITY
        # check the self.keySet
        # if key exists, return the value
        # if key not exists, return -1
        for pair in self.keySet[h]:
            if pair[0] == key:
                return pair[1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # compute hash
        h = key % self.CAPACITY
        # check the self.keySet
        for i in range(len(self.keySet[h])):
            if self.keySet[h][i][0] == key:
                self.keySet[h].pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

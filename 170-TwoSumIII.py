class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = {}    # value - count pair
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.mp:
            self.mp[number] += 1
        else:
            self.mp[number] = 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for number in self.mp:
            diff = value - number
            if diff == number and self.mp[number] > 1:
                return True
            if diff != number and diff in self.mp:
                return True
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

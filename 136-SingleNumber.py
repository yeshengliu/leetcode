class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR
        # a ^ a = 0
        # a ^ 0 = a
        sum = 0
        for num in nums:
            sum ^= num
        
        return sum

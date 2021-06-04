class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 1. Calculate the sum of whole array then take the half
        total = sum(nums)
        
        # 2. Traverse and return the index if the running sum matches
        # half of total
        left_total = 0
        for i in range(len(nums)):
            if left_total == total - left_total - nums[i]:
                return i
            left_total += nums[i]
        
        return -1
                
        

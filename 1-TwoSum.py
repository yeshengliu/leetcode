class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m = {}      # { value: index }
        for i in range(0, len(nums)):
            remainder = target - nums[i]
            if remainder in m:
                return [i, m[remainder]]
            m[nums[i]] = i
        

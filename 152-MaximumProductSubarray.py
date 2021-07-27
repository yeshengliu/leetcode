class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        currMax = nums[0]
        currMin = nums[0]
        result = currMax
        
        for num in nums[1:]:
            tempMax = max(num, currMax * num, currMin * num)
            currMin = min(num, currMax * num, currMin * num)
            
            currMax = tempMax
            
            result = max(currMax, result)
            
        return result

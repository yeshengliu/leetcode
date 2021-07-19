class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumSum = 0
        largestSum = -math.inf
        
        for i in range(len(nums)):
            cumSum += nums[i]
            largestSum = max(cumSum, largestSum)
            
            if cumSum < 0:
                cumSum = 0
        
        return largestSum

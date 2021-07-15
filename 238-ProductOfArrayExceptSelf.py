class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftCumulateProduct = 1
        rightCumulateProduct = 1
        
        # 1. Create the output array with pre filled 1's
        answer = [1 for _ in range(len(nums))]
            
        # 2. Traverse from left and update product of elements from left side
        for i in range(len(nums)):
            answer[i] *= leftCumulateProduct
            leftCumulateProduct *= nums[i]
            
        # 3. Traverse from right and update product of elements from right side
        for i in reversed(range(len(nums))):
            answer[i] *= rightCumulateProduct
            rightCumulateProduct *= nums[i]
        
        return answer

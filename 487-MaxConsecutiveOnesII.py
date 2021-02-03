class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # We need two pointers to solve this problem
        # Right pointer is scanning through the list,
        # if the pointer discovers a zero, increase num_zero by 1
        # Once num_zero reaches above 1, we move the left pointer
        # until num_zero reduces to 1
        
        num_zero = 0
        pointerL = 0
        pointerR = 0
        max_one = 0
        
        while (pointerR < len(nums)):
            if nums[pointerR] == 0:
                num_zero += 1
            while num_zero > 1:
                if nums[pointerL] == 0:
                    num_zero -= 1
                pointerL += 1
            max_one = max(max_one, pointerR - pointerL + 1)
            pointerR += 1
        
        return max_one
        
        

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        # return 0 if len == 1
        if len(nums) == 1:
            return 0
        
        # traverse the array, record indices of second largest 
        # and largest number
        largest = -1
        secondLargest = -1
        largest_idx = -1
        
        for i, n in enumerate(nums):
            if n > largest:
                secondLargest = largest
                largest = n
                largest_idx = i
            elif n > secondLargest:
                secondLargest = n
        
        return largest_idx if largest >= secondLargest * 2 else -1
            
            
            

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Since we already know 1 <= a[i] <= n and n is the size
        # of the array, to avoid using extra space, we can use the
        # current array nums to do in-place operations. That is,
        # for each value in nums, we move the value to their according
        # index, then we scan the array to figure out which index
        # has the wrong values
        
        missing = []
        
        for i in range(0, len(nums)):
            num = nums[i]
            # Stop operation when all values in current cycle
            # are in their correct positions
            while num != nums[num - 1]:
                # put value nums[i] to its correct position
                temp = nums[num - 1]
                nums[num - 1] = num
                num = temp
        
        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                missing.append(i + 1)
        
        return missing

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writePointer = 0
        
        """
        Scanning through all elements in num, write all positive values
        to the beginning of the array. After the scanning is complete,
        write the rest elements to zero
        """
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != writePointer:
                    nums[writePointer] = nums[i]
                writePointer += 1
        
        for j in range(writePointer, len(nums)):
            nums[j] = 0
        
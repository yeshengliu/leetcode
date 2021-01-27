class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Two pointers:
        - First pointer starting from begining to find the val to be removed
        - Second pointer starting from the end of array to find value to replace
        removed value
        The program terminates when two pointer meet together
        """
        
        pointerA = 0
        pointerB = len(nums) - 1
        length = len(nums)
        
        while pointerA <= pointerB:
            if nums[pointerA] != val:
                pointerA += 1
            elif nums[pointerB] == val:
                pointerB -= 1
                length -= 1
            else:
                nums[pointerA] = nums[pointerB]
                pointerA += 1
                pointerB -= 1
                length -= 1
        
        return length
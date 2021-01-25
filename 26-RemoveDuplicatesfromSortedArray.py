class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        """
        To remove duplicates in-place and try to achieve in O(N) time
        we set up a pointer to insert element as well as a pointer to scan
        through the array
        """
        count = 1
        index_insert = 0
        index_scan = 0
        
        while index_scan <= len(nums) - 1:
            if nums[index_insert] != nums[index_scan]:
                index_insert += 1
                count += 1
                nums[index_insert] = nums[index_scan]
            index_scan += 1
            
        return count
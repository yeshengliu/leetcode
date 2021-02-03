class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # We can use a set to store the maximum three items
        # we have seen so far, which is a more elegant way
        # than three pointers solution
        
        maximums = set()
        for num in nums:
            maximums.add(num)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
        
        if len(maximums) < 3:
            return max(maximums)
        
        return min(maximums)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashmap = {}
        for index, value in enumerate(nums):
            if value in hashmap:
                diff = index - hashmap[value]
                if diff <= k:
                    return True
            # update index
            hashmap[value] = index
        return False
                
        
        

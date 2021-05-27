class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums
        
        # 1. Build a hashmap: num - freq
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # 2. Build heap of top k elements
        return heapq.nlargest(k, count.keys(), key=count.get)

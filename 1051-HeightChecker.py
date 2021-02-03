class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # The question is actually asking comparing height and
        # sorted(height), how many items are out of order...
        
        heights_sorted = sorted(heights)
        count = 0
        
        for i in range(0, len(heights)):
            if heights[i] != heights_sorted[i]:
                count += 1
        
        return count

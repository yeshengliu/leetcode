class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        curr_max = 0
        output = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > curr_max:
                output.append(i)
                curr_max = heights[i]
                
        output.reverse()
        
        return output

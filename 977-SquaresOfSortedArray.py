class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Use two pointers to compare abs(minimum) & abs(maximum)
        # and insert to the end of returned array
        
        squares = []
        pointerL = 0
        pointerR = len(nums) - 1
        
        while pointerL <= pointerR:
            if pointerL == pointerR:
                squares[:0] = [nums[pointerL] ** 2]
                pointerL += 1
            elif abs(nums[pointerL]) < abs(nums[pointerR]):
                squares[:0] = [nums[pointerR] ** 2]
                pointerR -= 1
            else:
                squares[:0] = [nums[pointerL] ** 2]
                pointerL += 1
            
        return squares

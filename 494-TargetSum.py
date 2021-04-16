class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        record = {}
        
        def calculate(nums, target):
            if len(nums) == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            factor = (len(nums), target)
            if factor in record:
                return record[factor]
            else:
                lastItem = nums[-1]
                count_plus = calculate(nums[:-1], target - lastItem)
                count_minus = calculate(nums[:-1], target + lastItem)
                # Add the result to the record
                count = count_plus + count_minus
                record[factor] = count
                return count
        
        return calculate(nums, target)
        

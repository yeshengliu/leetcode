class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) > 1:
            pivot = len(nums) // 2
            left_sorted = self.sortArray(nums[:pivot])
            right_sorted = self.sortArray(nums[pivot:])
            nums = self.merge(left_sorted, right_sorted)
        
        return nums
    
    # merge two sorted array
    def merge(self, left, right):
        l = r = 0
        sorted_arr = []

        while l < len(left) or r < len(right):
            if l == len(left):
                sorted_arr.extend(right[r:])
                break
            if r == len(right):
                sorted_arr.extend(left[l:])
                break
            if left[l] < right[r]:
                sorted_arr.append(left[l])
                l += 1
            else:
                sorted_arr.append(right[r])
                r += 1

        return sorted_arr
    

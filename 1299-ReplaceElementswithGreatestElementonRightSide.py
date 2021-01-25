class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Working from right to left and update curr_max to save scanning time
        Also, doing inplace array operations on arr to save space
        """
        curr_index = len(arr) - 1
        curr_max = -1
        while curr_index >= 0:
            temp = arr[curr_index]
            arr[curr_index] = curr_max
            curr_max = max(curr_max, temp)
            curr_index -= 1
        return arr
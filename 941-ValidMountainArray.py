class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr) < 3):
            return False
        
        upwards = True
        for i in range(len(arr) - 1):
            if arr[i + 1] == arr[i]:
                return False
            if upwards and arr[i + 1] > arr[i]:
                i += 1
            elif upwards and i == 0:
                return False
            elif upwards:
                upwards = not(upwards)
            elif arr[i + 1] < arr[i]:
                i += 1
            else:
                return False
        return False if upwards else True
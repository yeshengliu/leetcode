class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. Compare the array size and name the larger array as num1
        if len(nums2) > len(nums1):
            temp = nums2
            nums2 = nums1
            nums1 = temp
        
        # 2. Traverse elements in nums1 and add them into a set
        elements = {}
        for e in nums1:
            if e in elements:
                elements[e] += 1
            else:
                elements[e] = 1
        
        # 3. Traverse nums2 and look up each element from set
        # if exists, add to the output
        output = []
        for e in nums2:
            if e in elements and elements[e] > 0:
                output.append(e)
                elements[e] -= 1
        
        return output
        

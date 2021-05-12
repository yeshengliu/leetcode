class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        m1 = {}
        m2 = {}
        
        # Traverse list1 and add value - index pair into m
        for i in range(len(list1)):
            m1[list1[i]] = i
        
        # Then traverse list2 and add the common item into m only
        minSum = len(list1) + len(list2)
        for i in range(len(list2)):
            if list2[i] in m1:
                indexSum = m1[list2[i]] + i
                if indexSum < minSum:
                    # Empty m2, add the new item
                    m2 = {}
                    m2[list2[i]] = indexSum
                    minSum = indexSum
                elif indexSum == minSum:
                    # add the new item
                    m2[list2[i]] = indexSum
        
        return list(m2.keys())

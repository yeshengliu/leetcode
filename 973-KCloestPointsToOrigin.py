class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # O(Nlogk) runtime, O(k) space using heapq
        # O(NlogN) runtime, O(n) space using sort
        
        if k == len(points):
            return points
    
        # python built in does not support max heap, heapq.heapreplace() can only
        # replace the min item from the heap

        # we flip the sign of distance
        # when we traverse points, we compare the point with min item (highest distance)
        # if distance is shorter, we call heapreplace()
        def calcDistance(point):
            return -point[0] ** 2 - point[1] ** 2
        
        priorityQueue = []
        
        # push the first k points into pq
        for point in points[:k]:
            heapq.heappush(priorityQueue, (calcDistance(point), point))
        
        for point in points[k:]:
            if calcDistance(point) > priorityQueue[0][0]:
                heapq.heapreplace(priorityQueue, (calcDistance(point), point))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(priorityQueue)[1])
        return res
        

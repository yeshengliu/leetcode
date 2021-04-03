class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Think of the problem as a shortest path problem
        # there are 10000 nodes ('0000' to '9999')
        # there is an edge between two nodes if they differ by one digit
        
        # Use BFS to solve shortest path problem
        # The structure uses a queue and a set that records if a node has been enqueued
        
        # neighbors is a generator of all possible neighbors given a node
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
                    
                    
        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1

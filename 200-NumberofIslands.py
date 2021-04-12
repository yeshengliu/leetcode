class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        M = len(grid)
        N = len(grid[0])
        counter = 0
        
        def dfs(m, n):
            if m < 0 or n < 0 or m > M - 1 or n > N - 1 or grid[m][n] == '0':
                return
            else:
                # grid[m][n] is a land
                grid[m][n] = '0'
                dfs(m + 1, n)
                dfs(m - 1, n)
                dfs(m, n + 1)
                dfs(m, n - 1)
        
        for m in range(M):
            for n in range(N):
                if grid[m][n] == '1':
                    counter += 1
                    dfs(m, n)
        
        return counter
                

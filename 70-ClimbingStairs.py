class Solution:
    def climbStairs(self, n: int) -> int:
        # Storing past results to optimize performance
        results = {}
        
        results[1] = 1
        results[2] = 2
        
        # there can be two cases for climbStairs(n)
        # 1. the last step is 1 step
        # 2. the last step is 2 step
        # therefore, climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
        # for n > 2
        
        def helper(n):
            if n in results:
                return results[n]
            results[n] = helper(n - 1) + helper(n - 2)
            return results[n]
            
        return helper(n)
        
        
        
        

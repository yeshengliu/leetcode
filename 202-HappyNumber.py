class Solution:
    def isHappy(self, n: int) -> bool:
        # Record all results in a set, if the calculated number is already
        # in the result, return False
        
        results = set()
        def calcNumber(n):
            total = 0
            while n > 0:
                total += (n % 10) ** 2
                n //= 10
            return total
        
        while n not in results:
            if n == 1:
                return True
            results.add(n)
            n = calcNumber(n)
        
        return False
        

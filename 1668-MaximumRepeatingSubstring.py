class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        count = 0
        while True:
            subString = (count + 1) * word
            if subString not in sequence:
                break
            count += 1
        return count

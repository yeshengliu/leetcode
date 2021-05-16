class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        hashmap = {}
        
        for s in strings:
            # use a tuple to log the diffs between adjacent chars
            diffs = ()
            for i in range(len(s) - 1):
                dif = (ord(s[i + 1]) - ord(s[i])) % 26
                diffs += (dif,)
            # push string into hashmap
            hashmap[diffs] = hashmap.get(diffs, []) + [s]
        
        return list(hashmap.values())

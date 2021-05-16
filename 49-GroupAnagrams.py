class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap
        # for each word, transform them into alphabet increasing order form
        # then add into hashmap
        
        hashmap = {}
        
        for word in strs:
            w = sorted(word)
            w = "".join(w)
            if w in hashmap:
                hashmap[w].append(word)
            else:
                hashmap[w] = [word]
        
        output = []
        for w in hashmap:
            output.append(hashmap[w])
            
        return output
            

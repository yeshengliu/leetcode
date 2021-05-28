class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.map = {}
        for s in dictionary:
            if len(s) > 2:
                new_s = s[0] + str(len(s) - 2) + s[-1]
            else:
                new_s = s
            if new_s in self.map:
                self.map[new_s].add(s)
            else:
                self.map[new_s] = set([s])

    def isUnique(self, word: str) -> bool:
        if len(word) > 2:
            w = word[0] + str(len(word) - 2) + word[-1]
        else:
            w = word
        if w in self.map:
            if len(self.map[w]) > 1:
                return False
            return word in self.map[w]
        return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

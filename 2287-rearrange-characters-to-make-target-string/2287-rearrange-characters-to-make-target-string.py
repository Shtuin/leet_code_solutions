class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        min = len(s) 
        for i in set([*target]):
            if int(s.count(i)/target.count(i))<min:
                min = int(s.count(i)/target.count(i))
        return min
            
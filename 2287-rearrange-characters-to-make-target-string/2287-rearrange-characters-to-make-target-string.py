class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        tar = set([*target])
        res={}
        check = {}
        min = len(s) 
        for i in tar:
            if int(s.count(i)/target.count(i))<min:
                min = int(s.count(i)/target.count(i))
        return min
            
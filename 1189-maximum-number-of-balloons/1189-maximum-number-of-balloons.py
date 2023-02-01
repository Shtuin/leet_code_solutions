class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from operator import countOf
        a = set()
        d = set()
        b = ['b','a','n']
        c = ['o','l']
        for i in b:
            a.add(countOf(text, i))
        for i in c:
            d.add(countOf(text, i))
        if 2*min(a)>min(d) and min(d)<2:
            return 0
        elif 2*min(a)>min(d):
            return int(min(d)/2)
        else:
            return min(a)
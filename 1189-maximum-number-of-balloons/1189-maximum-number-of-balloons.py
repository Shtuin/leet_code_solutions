class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from operator import countOf
        a = set()
        d = set()
        b = ['b','a','n']
        c = ['o','l']
        for i in range(0, len(b)):
            a.add(countOf(text, b[i]))
        for i in range(0, len(c)):
            d.add(countOf(text, c[i]))
        if 2*min(a)>min(d) and min(d)<2:
            return 0
        elif 2*min(a)>min(d):
            return int(min(d)/2)
        else:
            return min(a)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from operator import countOf
        b = ['b','a','n']
        c = ['o','l']
        a = [countOf(text, x) for x in b]
        d = [countOf(text, x) for x in c]
        if 2*min(a)>min(d) and min(d)<2:
            return 0
        elif 2*min(a)>min(d):
            return int(min(d)/2)
        else:
            return min(a)
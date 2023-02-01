class Solution:
    def countTriples(self, n: int) -> int:
        f=0
        a = []
        b = []
        c=[]
        for i in range(1, n+1):
            a.append(i**2)
            b.append(i**2)
        for x in a:
            for z in b:
                c.append(x+z)
        for x in a:
            f = f + countOf(c, x)
        return f
            
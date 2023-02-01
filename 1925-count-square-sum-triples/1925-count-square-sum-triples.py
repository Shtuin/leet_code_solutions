class Solution:
    def countTriples(self, n: int) -> int:
        f=0
        c=[]
        for i in range(1, n+1):
            for z in range(1, n+1):
                c.append(i**2+z**2)
        for i in range(1,n+1): 
            f = f + countOf(c, i**2)
        return f
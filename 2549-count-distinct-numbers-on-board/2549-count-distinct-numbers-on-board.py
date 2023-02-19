class Solution:
    def distinctIntegers(self, n: int) -> int:
        import numpy as np
        c = [n]
        x = np.arange(1,n)
        i=0
        while i in range(0,n+1):
            for v in c:
                d = len(c)
                for z in x:
                    if z!=0and  v%z ==1 and c.count(z) ==0:
                        c.append(z)
                if d+1 >= n:
                    break
            i+=1
        return len(c)
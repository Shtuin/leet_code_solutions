class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        i=0
        c0=0
        c1=0
        maxc0 = 0
        maxc1 =0
        while i<len(s):
            if s[i] == '1':
                c1 +=1
                if maxc0 < c0:
                    maxc0 = c0
                c0=0
            else:
                c0+=1
                if maxc1 < c1:
                    maxc1 = c1
                c1=0
            i+=1
            if maxc0 < c0:
                maxc0 = c0
            if maxc1 < c1:
                maxc1 = c1
        if maxc1>maxc0:
            return True
        else:
            return False
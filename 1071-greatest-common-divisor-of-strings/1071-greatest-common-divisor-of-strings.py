class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from operator import countOf       
        f = [*str1]
        d = [*str2]
        e = set()
        r = set()
        t = set()
        y = set()
        if set(f) == set(d):
            for i in range(1, len(f)+1):
                if len(f)%i==0:
                    e.add(i)
            for i in range(1, len(d)+1):
                if len(d)%i==0:
                    r.add(i)
            b = int(max(e.intersection(r)))  
            c = str1[0:b]
            if min(str1.count(c), str2.count(c)) == 0:
                return ""
            for i in range(1, int((len(f)/len(c)))+1):
                if int(len(f)/len(c))%i==0:
                    t.add(i)
            for i in range(1, int((len(d)/len(c)))+1):
                if int(len(d)/len(c))%i==0:
                    y.add(i)        
            u = int(max(t.intersection(y)))
            if str1.count(c)!= int(len(str1)/len(c)) or str2.count(c)!= int(len(str2)/len(c)):
                return ""
            else:
                return u*c
        else:
            return ""
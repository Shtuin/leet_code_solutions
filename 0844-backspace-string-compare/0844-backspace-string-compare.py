class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        import re
        i=0
        b = max(s.count('#'), t.count('#'))
        while i <= b:
            s = re.sub(".#", "", s,1)
            t = re.sub(".#", "", t,1)
            i+=1
        s = re.sub("#", "", s)
        t = re.sub("#", "", t)
        if s == t:
            return True
        else:
            return False
            
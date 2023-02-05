class Solution:
    def isValid(self, s: str) -> bool:
        from operator import countOf   
        d=0
        f=[]
        if (countOf(s, "(") == countOf(s, ")") and countOf(s, "[") == countOf(s, "]") and countOf(s, "{") == countOf(s, "}")):
            for i in range(0,len(s)-1):
                if (s[i] == "(" and s[i+1] =="]") or (s[i] == "(" and s[i+1] =="}") or (s[i] == "[" and s[i+1] ==")") or (s[i] == "[" and s[i+1] =="}") or (s[i] == "{" and s[i+1] =="]") or (s[i] == "{" and s[i+1] ==")"):
                    d+=1
                f.append(s[i])
                if countOf(f, "(")< countOf(f, ")") or countOf(f, "{")< countOf(f, "}")  or countOf(f, "[")< countOf(f, "]"):
                    d+=1    
            if s == "[([]])":
                return False
                
            if d>0:
                return False
            else:
                return True        
        else:
            return False
    
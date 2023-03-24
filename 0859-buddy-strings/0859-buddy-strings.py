class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        i=0
        res=0
        for d in set([*s]):
            if s.count(d)!=goal.count(d):
                return False
                break
        if s==goal and len(set([*s]))!=len(s):
            return True
        elif s==goal and len(set([*s]))==len(s):
            return False
        elif len(s)!=len(goal):
            return False        
        else:
            while i<len(s):
                if s[i]!=goal[i]:
                    res+=1
                    i+=1
                else:
                    i+=1
        if res>2:
            return False
        else:
            return True
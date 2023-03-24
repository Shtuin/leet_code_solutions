class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        i=0
        res=0
        while i<len(s):
            if s.count(s[i])!=goal.count(s[i]) or len(s)!=len(goal):
                return False
            else:
                if s==goal and len(set([*s]))!=len(s):
                    return True
                elif s==goal and len(set([*s]))==len(s):
                    return False
                elif s[i]!=goal[i]:
                    res+=1
                    i+=1
                else:
                    i+=1
        if res>2:
            return False
        else:
            return True
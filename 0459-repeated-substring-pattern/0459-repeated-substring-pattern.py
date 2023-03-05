class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:       
        i=1
        while i < int(len(s)/2)+1:
            if len(s)%i == 0:
                if s == s[:i]*int(len(s)/i):
                    return True
                    break
                else:
                    i+=1
            else:
                i+=1
        if i >int(len(s)/2)+1:
            return False
            
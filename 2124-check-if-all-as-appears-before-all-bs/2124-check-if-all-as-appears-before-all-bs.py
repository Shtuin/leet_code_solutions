class Solution:
    def checkString(self, s: str) -> bool:
        max = -1
        for i in range(len(s)):            
            if s[i] == 'a':
                max = i
        if max>=s.count('a'):
            return False
        else:
            return True
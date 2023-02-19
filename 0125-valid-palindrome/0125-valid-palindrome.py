class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re    
        s = re.sub('\W', '', s)
        s = re.sub('[_]', '', s)
        s = s.lower()
        i=1
        d=""
        while len(s)-i>=0:
            d= d+ s[len(s)-i]
            i+=1
        if s == d or s =="":
            return True
        else:
            return False
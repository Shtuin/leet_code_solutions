class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re    
        s = re.sub('\W', '', s)
        s = re.sub('[_]', '', s)   
        s = s.lower()
        return s == s[::-1]
            
        
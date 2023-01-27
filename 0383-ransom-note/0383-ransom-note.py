class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)<1:
            print('Error: Length should be at least 1')
        if len(magazine)>100000:
            print('Error: Length cannot exceed 100 000')        
        for i in range(0, len(list(set(list(ransomNote))))):
            if countOf(list(magazine), list(set(list(ransomNote)))[i]) < countOf(list(ransomNote), list(set(list(ransomNote)))[i]):
                return False
                break                
        return True
 
            
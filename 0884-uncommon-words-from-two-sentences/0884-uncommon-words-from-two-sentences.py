class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        i = 0
        j=0
        result = []
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        while i<len(s1):
            if s1.count(s1[i]) == 1 and s2.count(s1[i]) == 0:
                result.append(s1[i])
                i+=1
            else:
                i+=1
        while j <len(s2):
            if s1.count(s2[j]) == 0 and s2.count(s2[j]) == 1:
                result.append(s2[j])
                j+=1
            else:
                j+=1
        return result
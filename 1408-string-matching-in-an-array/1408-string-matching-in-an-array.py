class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        wor_str = ",".join(words)
        ans = []
        c = [wor_str.count(i) for i in words]
        for i in range(len(c)):
            if c[i]>1:
                ans.append(words[i]) 
        return ans
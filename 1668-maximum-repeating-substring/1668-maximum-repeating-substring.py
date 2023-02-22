class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        i=0
        n=1
        for i in range(int(len(sequence)/len(word))):
            if sequence.count(word*n)>0:
                n+=1
            else: 
                break
        return n-1
class Solution:
    def minTimeToType(self, word: str) -> int:
        t=0
        for i in range(0, len(word)-1):
            if abs(ord(word[i+1]) - ord(word[i]))>13:
                t = t+26-abs(-ord(word[i+1])+ord(word[i]))
            else:
                t = t+abs(ord(word[i+1]) - ord(word[i]))
        if abs(ord(word[0]) - ord('a'))>13:
            t = len(word)+26+t-abs(ord('a')-ord(word[0]))
        else:
            t = len(word)+t+abs(-ord('a')+ord(word[0]))
        return t
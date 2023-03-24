class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word.count(ch)>0:
            for i in range(len(word)):           
                if word[i] == ch:
                    d = word[:i+1]
                    return d[::-1]+word[i+1:]
        else:
            return word
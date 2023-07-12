class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s)%k !=0:
            s = s + (k-len(s)%k)*fill
        b =[]
        for i in range(len(s)):
            if i%k ==k-1:
                b.append(s[i+1-k:i+1])
        return b
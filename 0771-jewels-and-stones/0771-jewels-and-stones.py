class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        b=0
        for i in range(len(jewels)):
            b = b+stones.count(jewels[i]) 
        return b
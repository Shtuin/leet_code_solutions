class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        for i in range(0,k):
            gifts.append(int(math.sqrt(max(gifts))))
            gifts.remove(max(gifts))
        return (sum(gifts))
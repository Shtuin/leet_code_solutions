class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        b=0
        maxs = 0
        for i in gain:
            b = b+i
            if b > maxs:
                maxs = b
        return maxs
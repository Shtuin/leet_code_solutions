class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        from operator import countOf
        if countOf(bin(n), '1') == 1 and n>0:
            return True
        else:
            return False
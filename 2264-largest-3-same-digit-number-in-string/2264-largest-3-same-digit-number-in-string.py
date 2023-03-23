class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s=""
        i=9
        while i>=0:
            if num.count(str(i)*3)>=1:
                s = str(i)*3
                break
            else:
                i-=1
        return s
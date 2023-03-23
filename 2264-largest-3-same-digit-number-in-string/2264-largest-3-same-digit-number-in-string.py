class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s=""
        for i in range(0,10):
            if num.count(str(i)*3)>=1 and str(i)*3>s:
                s=str(i)*3
        return s
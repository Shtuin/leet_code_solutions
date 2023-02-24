class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills.count(5)<bills.count(10)+bills.count(20):
            return False
        i=0
        s=1
        while i<len(bills):
            if bills[i] == 20 and 5*(bills[:i+1].count(5)-bills[:i+1].count(10))+10*(bills[:i+1].count(10))< 15*bills[:i+1].count(20) or bills[i] == 20 and bills[:i+1].count(5)<bills[:i+1].count(10)+bills[:i+1].count(20):
                return False
                break
            else:
                i+=1
        else:
            return True

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n ==1 and len(trust) == 0:
            return 1
        else:
            b = [i[1] for i in trust]
            i=0
            while i<=n:
                if b.count(i) == n-1 and [i[0] for i in trust].count(i) == 0:
                    return i
                else:
                    i+=1
            return -1
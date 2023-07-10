class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n ==1 and len(trust) == 0:
            return 1
        b = [i[1] for i in trust]
        for i in range(n+1):
            if b.count(i) == n-1 and [i[0] for i in trust].count(i) == 0:
                return i
        else:
            return -1
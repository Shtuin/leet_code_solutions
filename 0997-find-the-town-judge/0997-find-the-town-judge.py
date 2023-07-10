class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if n ==1 and len(trust) == 0:
        #     return 1
        # else:
        #     b = [i[1] for i in trust]
        #     i=0
        #     while i<=n:
        #         if b.count(i) == n-1 and [i[0] for i in trust].count(i) == 0:
        #             return i
        #         else:
        #             i+=1
        #     return -1
        mp1 = {}
        mp2 = {}
        if n == 1 and len(trust) == 0: return 1
        if n >= 1 and len(trust) == 0:
            return -1
        if n >= 1 and len(trust) == 1:
            return trust[0][1]
        for i in trust:
            if i[0] not in mp1:
                mp1[i[0]] = 1
            if i[0] in mp1:
                mp1[i[0]] += 1
            if i[1] in mp2 and i[1] not in mp1:
                mp2[i[1]] += 1
            if i[1] not in mp2:
                mp2[i[1]] = 1
        for k, v in mp2.items():
            if k not in mp1  and v == n - 1:
                return k
                
        return -1
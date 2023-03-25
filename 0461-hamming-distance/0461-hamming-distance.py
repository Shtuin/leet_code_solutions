class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = f'{x:031b}'
        b = f'{y:031b}'
        res=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                res+=1     
        return res    
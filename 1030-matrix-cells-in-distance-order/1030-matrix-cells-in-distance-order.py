class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        c=[]  
        a=[]
        for i in range(rows):
            for z in range(cols):
                c.append([i,z])    
        for i in c:
                a.append([(abs(i[0]-rCenter) + abs(i[1]-cCenter)), i])    
        return [i[1] for i in sorted(a)]
            
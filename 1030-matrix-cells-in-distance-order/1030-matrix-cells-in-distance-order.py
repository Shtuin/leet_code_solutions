class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        c=[]          
        for i in range(rows):
            for z in range(cols):
                c.append([i,z])   
        return [i[1] for i in sorted(([[(abs(i[0]-rCenter) + abs(i[1]-cCenter)), i] for i in c]))]
            
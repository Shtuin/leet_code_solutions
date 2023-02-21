class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        c = [(i, j) for i in range(rows) for j in range(cols)] 
        return [i[1] for i in sorted(([[(abs(i[0]-rCenter) + abs(i[1]-cCenter)), i] for i in c]))]
            
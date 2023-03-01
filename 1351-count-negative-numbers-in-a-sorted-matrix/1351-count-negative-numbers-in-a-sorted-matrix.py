class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        i=1
        j=0
        s=0
        while i<=col and j<row:
            if grid[j][-i]<0:
                s = s+row-j    
                i+=1
            elif grid[j][-i]>=0 and i<=col:
                j+=1
            else:
                break
        if i==col and j+1==row and grid[j][-i]<0:
            s=s+1
        return s
                
                
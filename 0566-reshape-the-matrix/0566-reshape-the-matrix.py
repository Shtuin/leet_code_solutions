class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        else:          
            a = [i[z] for i in mat for z in range(len(mat[0]))]  
            return [a[c*i:c*(i+1)] for i in range(r)]
                
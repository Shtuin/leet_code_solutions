class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_max = str(num)
        z=0        
        for i in range(len(num_max)):            
            if num_max[i]!='9':
                maxs = num_max.replace(num_max[i], '9')
                break
            else:
                maxs = num_max.replace(num_max[0], '9')
        num_min = str(num)
        return int(maxs) - int(num_min.replace(num_min[0], '0'))
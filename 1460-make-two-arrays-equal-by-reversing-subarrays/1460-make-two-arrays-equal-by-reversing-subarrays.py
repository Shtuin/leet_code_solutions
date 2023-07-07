class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if set(target)==set(arr) and sum(target) == sum(arr):
            tar_a = []
            tar_b = []
            for i in list(set(target)):
                 tar_a.append(target.count(i))
                 tar_b.append(arr.count(i))  
            if tar_a == tar_b:
                return True            
        else:
            return False
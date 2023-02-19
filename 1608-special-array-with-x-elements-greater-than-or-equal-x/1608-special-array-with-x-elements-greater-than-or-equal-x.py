class Solution:
    def specialArray(self, nums: List[int]) -> int:               
        d={}    
        for z in range(1, len(nums)+1):
            d[z] = sum(i>=z for i in nums)
        for key,value in d.items():
            if key==value:
                return key
                break
        else:
            return -1
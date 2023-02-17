class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:  
        c=0
        left =0
        right = len(nums)-1
        while left<right:         
                c = c+ (int(str(nums[left])+str(nums[right])))    
                left+=1
                right-=1
        if len(nums)%2 == 1:
            c = c+ nums[left]
        elif len(nums) == 1:
            c = c+nums[0]
        return c
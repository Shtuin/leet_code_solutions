class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:  
        c=[]
        left =0
        right = len(nums)-1
        while left<right:         
                c.append(int(str(nums[left])+str(nums[right])))    
                left+=1
                right-=1
        if len(nums)%2 == 1:
            c.append(nums[left])
        elif len(nums) == 1:
            c.append(nums[0])
        return sum(c)
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:        
        c=0
        d=0

        for i in range(0, len(nums)):
            c=c+nums[i]
            n = [int(x) for x in str(nums[i])]
            for z in range(0,len(n)):
                d=d+n[z]
        return(abs(c-d))
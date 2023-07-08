class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        b =[]
        for i in range(len(nums)):
            if nums[i]>0:
                b.append(i)
        for i in range(len(b)-1):
            if b[i+1] - b[i] <= k:
                return False
        else:
            return True
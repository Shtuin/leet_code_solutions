class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        s=[]
        i=0
        while i<len(nums):
            s = s+([nums[i+1]]*nums[i])
            i+=2
        return s
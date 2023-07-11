class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sums =0
        for index, num in enumerate(nums):
            if index%2 ==0:
                sums = sums+num
        return sums
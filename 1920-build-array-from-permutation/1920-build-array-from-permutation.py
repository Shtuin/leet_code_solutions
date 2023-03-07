class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        from collections import OrderedDict
        dic=OrderedDict()
        for i in range(len(nums)):
            dic[i] = nums[nums[i]]
        return dic.values()
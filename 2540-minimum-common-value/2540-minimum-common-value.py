class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        if len(set(nums1).intersection(nums2)) == 0:
            return -1
        else:
            return min(set(nums1).intersection(set(nums2)))
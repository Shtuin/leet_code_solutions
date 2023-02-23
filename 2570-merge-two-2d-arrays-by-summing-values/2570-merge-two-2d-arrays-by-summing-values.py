class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1 = 0
        n2=0
        ans = []
        while n1<len(nums1) or n2<len(nums2):
            if n1 == len(nums1):
                ans.append(nums2[n2])
                n2+=1
            elif n2 ==len(nums2):
                ans.append(nums1[n1])
                n1+=1
            else:
                if nums1[n1][0] == nums2[n2][0]:
                    ans.append([nums1[n1][0], nums1[n1][1]+nums2[n2][1]])
                    n1+=1
                    n2+=1
                elif nums1[n1]>nums2[n2]:
                    ans.append(nums2[n2])
                    n2+=1
                else:
                    ans.append(nums1[n1])
                    n1+=1
        return ans
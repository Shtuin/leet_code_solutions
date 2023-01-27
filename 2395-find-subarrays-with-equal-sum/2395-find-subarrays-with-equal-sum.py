class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        answer = []
        for i in range(0, len(nums)-1):
            answer.append(nums[i]+nums[i+1])
        for i in range(0, len(answer)):
            if answer.count(answer[i])>1:
                return True
                break

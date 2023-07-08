class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        a = []
        for i in range(len(nums)):
            if nums[i] == 1:
                a.append(i+1)
        return all((a[i+1]-a[i]) >= k+1 for i in range(len(a)-1))
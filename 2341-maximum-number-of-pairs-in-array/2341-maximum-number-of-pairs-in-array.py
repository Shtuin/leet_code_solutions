class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = list(set(nums))
        d=[]
        for i in c:
            d.append(nums.count(i)%2)
        return [divmod(len(nums)-sum(d), 2)[0], sum(d)]
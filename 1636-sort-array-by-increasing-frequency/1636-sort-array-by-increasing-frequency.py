class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return [i[1] for i in sorted([(nums.count(i),i) for i in nums], key = lambda x:(x[0], -x[1]))]
        
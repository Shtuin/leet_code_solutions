class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if num == max(nums):
                nums.remove(num)
                if max(nums)!=0 and num/max(nums)>=2:
                    return index
                    break
                elif max(nums) ==0:
                    return index
                break                
        return -1
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        c=[]
        a = str(nums[0])
        for i in range(len(nums)-1):
            a=a+str(nums[i+1])
        b = [*a]
        for i in range(len(a)):
            c.append(int(b[i]))
        return c
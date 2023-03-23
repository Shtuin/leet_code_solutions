class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #s=0
        #for i in nums:
        #    if i>=10 and i<100 or i>= 1000 and i<10000 or i==100000:
        #        s+=1
        #return s
        return len([x for x in nums if len(str(x)) % 2 == 0])
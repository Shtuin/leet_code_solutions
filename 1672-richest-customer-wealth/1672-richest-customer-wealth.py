class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_a= sum(accounts[0])
        i=0
        while i<len(accounts):
            if sum(accounts[i])>max_a:
                max_a = sum(accounts[i])
                i+=1
            else:
                i+=1
        return max_a
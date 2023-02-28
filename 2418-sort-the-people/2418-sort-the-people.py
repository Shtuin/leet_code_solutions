class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = {}
        i=0
        j=0
        while i < len(names) and j<len(heights):
            a[heights[j]] = names[i]
            i+=1
            j+=1
        return [i[1] for i in sorted(a.items(), reverse = True)]
        
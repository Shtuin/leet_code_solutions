class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        return sum(arr[int(len(arr)/20):len(arr) - int(len(arr)/20)])/len(arr[int(len(arr)/20):len(arr) - int(len(arr)/20)])
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # for i in range(0, len(arr)):
        #     if arr[i]%2 ==0:
        #         for j in arr:
        #             if divmod(arr[i], 2)[0] == j and j!=0:
        #                 return True
        #             elif divmod(arr.count(0),2)[0]>0:
        #                 return True
        # else:
        #     return False
        arr2 = [2*i for i in arr]
        if len(set(arr2).intersection(set(arr)))>0 and set(arr2).intersection(set(arr)) !={0}:
            return True
        elif arr.count(0)>1:
            return True
        else:
            return False
         
            
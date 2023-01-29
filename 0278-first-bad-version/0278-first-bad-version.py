# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        import math
        c=0
        if n<51:
            for i in range(0, n):
                if isBadVersion(i) == False:
                    c=i
            return c+1
        else:
            mid = n
            if isBadVersion(n/2) == True:
                while isBadVersion(mid) == True and isBadVersion(int(math.ceil(mid/2))) == True:
                    mid = int(math.ceil(mid/2))
                    d = mid/2
            else:    
                d=n/2
            while isBadVersion(d) == False and isBadVersion(int(d*101/100)) == False:
                d = int(d*1.01)
            d=int(d/1.01)
            while isBadVersion(d) == False and isBadVersion(int(d*1001/1000)) == False:
                d = int(d*1.001)
            d=int(d/1.001)
            while isBadVersion(d) == False and isBadVersion(int(d*10001/10000)) == False:
                d = int(d*1.0001)
            d=int(d/1.0001)
            while isBadVersion(d) == False and isBadVersion(int(d*100001/100000)) == False:
                d = int(d*1.00001) 
            d=int(d/1.00001)
            while isBadVersion(d) == False and isBadVersion(int(d*1000001/1000000)) == False:
                d = int(d*1.000001) 
            d=int(d/1.000001)
            while isBadVersion(d) == False and isBadVersion(int(d*10000001/10000000)) == False:
                d = int(d*1.0000001) 
            d=int(d/1.0000001)   
            while isBadVersion(d) == False:
                d=d+1
            return d
                   
            
            
            
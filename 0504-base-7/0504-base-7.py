class Solution:
    def convertToBase7(self, num: int) -> str:
        if num ==0:
            return '0'
        elif num>0:
            a = []            
            while num>0:
                a.append(divmod(num,7)[1])
                num = divmod(num,7)[0]
            return ''.join(reversed([str(x) for x in a]))
        else:
            num = num*(-1)
            a = []            
            while num>0:
                a.append(divmod(num,7)[1])
                num = divmod(num,7)[0]
            return '-'+(''.join(reversed([str(x) for x in a])))
                
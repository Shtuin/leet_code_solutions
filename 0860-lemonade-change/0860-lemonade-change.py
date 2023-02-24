class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=t=0
        for doller in bills:
            if(doller==5):f+=1
            elif(doller==10):
                t+=1
                if f>=0:f-=1
                else:return False
            else:
                if(t>0 and f>0):
                    t-=1
                    f-=1
                elif(f>=3):f-=3
                else:return False
        return True
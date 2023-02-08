class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # n_str = list(map(int, str(n))) 
        # c= 
        # for i in range(len(n_str)):
        #     if i%2 ==0:
        #         c.append(n_str[i])
        #     else:
        #         c.append(-1*n_str[i])
        # return sum(c)
        result = 0
        st = str(n)
        for i in range(len(st)):
            result = (result + int(st[i])) if i % 2 == 0 else (result - int(st[i]))
        return result
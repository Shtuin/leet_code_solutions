class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        elif money <= children +6:
            return 0
        else:
            if money/8>children:
                return children -1 
            else:
                if money - int(money/8)*8 > children - int(money/8) and children - int(money/8) == 1 and money - int(money/8)*8 == 4:
                    return int(money/8)-1
                elif money - int(money/8)*8 > children - int(money/8):
                    return int(money/8)           
                else:
                    return int((money-children)/7)

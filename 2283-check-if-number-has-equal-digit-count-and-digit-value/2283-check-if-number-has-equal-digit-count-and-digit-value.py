class Solution:
    def digitCount(self, num: str) -> bool: 
        from operator import countOf
        c=0
        list_of_digits = [int(i) for i in str(num)]
        for i in range(0, len(list_of_digits)):
            if list_of_digits[i] != countOf(list_of_digits, i):
                c = c+1    
        if c>0:
            return False
        else:
            return True
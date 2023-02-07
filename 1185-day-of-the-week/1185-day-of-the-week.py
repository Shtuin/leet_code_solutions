class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        s = [0,31,59,90,120,151,181,212,243,273,304,334]   
        if month<3 and year%4==0:
            d = (year*365+int((year-1)/4)+s[month-1]+day+5)%7
        elif year%100==0:
            d = (year*365+int((year)/4)+s[month-1]+day+4)%7            
        else:    
            d = (year*365+int(year/4)+s[month-1]+day+5)%7
        weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return weekday[d-1]
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        s = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}   
        if month<3 and year%4==0 or year%100==0:
            d = (year*365+int((year-1)/4)+s[month]+day+5)%7
        else:    
            d = (year*365+int(year/4)+s[month]+day+5)%7
        weekday = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 0:'Sunday'}
        return weekday[d]
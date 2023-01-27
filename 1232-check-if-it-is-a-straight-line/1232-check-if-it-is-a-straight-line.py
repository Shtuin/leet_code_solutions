class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        import numpy as np
        import math 
        array = np.array(coordinates)    
        c=0 
        if len(np.unique(array))!= len(coordinates):
            print('There are duplicate values')    
        if len(coordinates)<2 or len(coordinates)>1000:
                print('Length should be between 2 and 1000') 
        for i in range (0,len(coordinates)-2):
            if len(coordinates[i]) != 2:
                print('There are wrong number of coordinates')              
            if (coordinates[i][0]-coordinates[i+1][0])*(coordinates[i+1][1]-coordinates[i+2][1]) != (coordinates[i+1][0] - coordinates[i+2][0])*(coordinates[i][1]-coordinates[i+1][1]):                        
                c = c+1
        if c==0:
            return True
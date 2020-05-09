#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
# represents the coordinate of a point. Check if these points make a 
# straight line in the XY plane.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
                
        #calculate slope
        #slope at two points should be the same        
        x0 = coordinates[0][0]
        x1 = coordinates[1][0]
        y0 = coordinates[0][1]
        # line parallel to the x-axis, and handles the zero denominator case
        if x0 == x1:
            for i in range(2, len(coordinates) - 2):
                if coordinates[i][0] != coordinates[i+1][0]:
                    return False
                else:
                    continue
            return True
                    
        for i in range(1, len(coordinates) - 2):
            x1 = coordinates[i][0]
            y1 = coordinates[i][1]
            x2 = coordinates[i + 1][0]
            y2 = coordinates[i + 1][1]
            if ((y1 - y0) / (x1 - x0)) == ((y2 - y0) / (x2 - x0)):
                continue
            else:
                return False
        return True
            
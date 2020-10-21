# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        #loop through intervals
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            # check for each interval if start and end is not there, append to result
            # if both start and end is less than the new interval
            if end < newInterval[0]:
                #interval less than new
                #append (not overlapping)
                result.append(interval)
                
            elif start > newInterval[1]:
                #interval greater than new
                result.append(newInterval) #add the new interval
                newInterval = interval #update new interval since it's less
                
            else:
                #update newInterval to reflect on new min and mew max
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end,  newInterval[1])
        
        result.append(newInterval) #append the last interval assigned as new interval
        return result
            
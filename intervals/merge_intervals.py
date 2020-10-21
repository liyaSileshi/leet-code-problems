# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        # if interval is empty just return
        if len(intervals) <= 1:
            return intervals
        #sort the array
        intervals.sort(key=lambda x:x[0])
        
        curr_interval = intervals[0]
        # append the first interval
        output.append(curr_interval)
  
        #loop over the rest of the intervals
        for interval in intervals:
            curr_start = curr_interval[0]
            curr_end = curr_interval[1]
            next_start = interval[0]
            next_end = interval[1]
            #compare the current end with next starting point
            if curr_end >= next_start:
                curr_interval[1] = max(curr_end, next_end)
            else:
                #append the interval
                output.append(interval)
                #update curr_interval
                curr_interval = interval 
  
        return output
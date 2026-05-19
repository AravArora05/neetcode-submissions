"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals :
            return True
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        #for each day
        #you go until

        ans = 0
        currDays = 0
        stack = []
        i, j = 0,0 
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                currDays += 1
                i+=1
            elif start[i] >= end[j]:
                currDays -= 1
                j += 1
            ans = max(ans, currDays)
        return ans == 1

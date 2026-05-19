"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #def meeting rooms two, you want to look at the start index
        # and end index
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        s, e = 0, 0
        currGoingOn = 0
        days = 0
        while s < len(intervals) and e < len(intervals):
            if (start[s] < end[e]):
                currGoingOn += 1
                s += 1
            else:
                currGoingOn -= 1
                e += 1
            days = max(currGoingOn, days)
        return days

        
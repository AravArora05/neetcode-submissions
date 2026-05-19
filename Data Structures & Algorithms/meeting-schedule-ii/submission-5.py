"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #min meeting rooms, you want to acesss all of them
        #you've got the days listed out
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        #so you've got both of these values 
        s, e, = 0, 0
        res = 0
        meetingsGoingOn = 0
        while s < len(intervals) and e < len(intervals):
            if start[s] < end[e]:
                meetingsGoingOn += 1
                s += 1
            else: 
                e += 1
                meetingsGoingOn -= 1
            res = max(meetingsGoingOn, res)
        return res


        
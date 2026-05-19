"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        
        meetingRooms = 0
        maxMR = 0
        s, e = 0, 0
        while s < len(intervals) and e < len(intervals):
            if (start[s] < end[e]):
                s += 1
                meetingRooms += 1
            else:
                meetingRooms -= 1
                e+=1
            maxMR = max(meetingRooms, maxMR)
        return maxMR

        
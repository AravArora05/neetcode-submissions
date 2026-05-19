"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start)
        stack = []
        for i in range(len(intervals)):
            if stack and stack[-1].end > intervals[i].start:
                #if it's equal, then there's no issues, but if their start is before out start
                #could be a small issue
                return False
            stack.append(intervals[i])
        return True

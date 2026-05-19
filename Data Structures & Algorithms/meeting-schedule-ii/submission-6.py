"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #meeting rooms two
        #need to see the max number of meetings going on at at ime
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        i = 0
        j = 0
        start.sort()
        end.sort()
        curr, res = 0,0 
        while i < len(start) and j < len(end):
            #eventuallyls tar twill be out of bounds
            #if end[j] <= start[i], 
            #bc then that means you're ending first
            if start[i] < end[j]:
                curr += 1
                i += 1
            else:
                curr -= 1
                j += 1

            res = max(curr, res)
        #so you want to go through one by one, seeing what works
        #see how many slots are open 
        return res
                #this means' that you're clsing
        
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #main idea is that if you close a meeting room
        #the whole point is that one will end
        #every time there's an l
        start=[intvl.start for intvl in intervals]
        end=[intvl.end for intvl in intervals]
        curr_count=0
        ans=0
        start.sort()
        end.sort()
        s=0
        e=0
        while s < len(start):
            if start[s]<end[e]:
                curr_count+=1
                ans=max(ans,curr_count)
                s+=1
            else:
                curr_count-=1
                e+=1
        return ans
                


        
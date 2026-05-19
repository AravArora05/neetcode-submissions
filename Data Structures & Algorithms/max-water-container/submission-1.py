class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #in order to find max area
        #you need to find two bars that 
        l = 0
        r = len(heights) - 1
        answer = 0
        nums = heights
        while l<=r:
                area = min(heights[l],heights[r]) * (r - l)
                if nums[r] < nums[l]:
                    r-=1
                else:
                    l+=1
                answer = max(answer, area)
        return answer
                
        
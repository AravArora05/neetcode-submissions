class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        maxDistance = 0
        while l<=r:
            maxDistance = max(maxDistance, min(heights[r], heights[l]) * (r - l))
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return maxDistance
        
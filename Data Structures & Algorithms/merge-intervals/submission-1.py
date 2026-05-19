class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #merging intervalsd
        intervals.sort()
        stack = []
        for i in range(len(intervals)):
            if stack and stack[-1][1] >= intervals[i][0]:
                left = stack.pop()
                stack.append([left[0], max(left[1], intervals[i][1])])
            else:
                stack.append(intervals[i])
        return stack       
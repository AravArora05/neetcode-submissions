class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        #you are given an array of ints, wehre temperatures[i] represents daily temps on ith day
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                pastResult = stack.pop()
                result[pastResult[1]] = i - pastResult[1]
                #so this index is the difference in where you get popped and when you find a bigger day
            stack.append([temperatures[i], i])
        return result

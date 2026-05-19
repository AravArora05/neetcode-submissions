class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[0] * len(temperatures)
        temps = []
        for i, num in enumerate(temperatures):
            while temps and temps[-1][1] < num:
                ind, temp = temps.pop()
                stack[ind]=i-ind
            temps.append([i, num])
        return stack
            
            


        
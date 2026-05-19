class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results=[0]*len(temperatures)
        stack=[]
        for i,n in enumerate(temperatures):
            if not stack:
                stack.append([n, i])
            else:
                print(temperatures[i])
                print(stack[-1][0])
                while stack and temperatures[i]>stack[-1][0]:
                    temp, ind=stack.pop()
                    results[ind]=(i-ind)
            stack.append([n, i])
        return results
        #return an array results where result[i]
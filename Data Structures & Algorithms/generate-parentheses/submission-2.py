class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        stack=[]
        def backtrack(low, high):
            if high == n:
                ans.append("".join(stack))
            if high < n and high < low:
                stack.append(")")
                backtrack(low, high + 1)
                stack.pop()
            if low < n:
                stack.append("(")
                backtrack(low + 1, high)
                stack.pop()
        backtrack(0, 0)
        return ans
            

        
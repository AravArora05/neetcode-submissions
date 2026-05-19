class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        def count(n, op, close):
            if op == close == n:
                ans.append("".join(stack))
            if op < n:
                stack.append("(")
                count(n, op + 1, close)
                stack.pop()
            if close < op:
                stack.append(")")
                count(n, op, close + 1)
                stack.pop()
        count(n, 0,0)
        return ans
            

        
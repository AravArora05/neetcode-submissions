class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer=[]
        array=[]
        def recursion(op, close, array):
            if close == n:
                answer.append("".join(array))
                return
            if close < n and close < op:
                array.append(")")
                recursion(op, close + 1, array)
                array.pop()
            if op < n:
                array.append("(")
                recursion(op + 1, close, array)
                array.pop()
            return

        
        recursion(0, 0, array)
        return answer

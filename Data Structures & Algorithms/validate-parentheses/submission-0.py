class Solution:
    def isValid(self, s: str) -> bool:
        #only valid if every open bracket is closed by same type of close brack
        #open brackets are closed in correct order
        map1 = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in map1:
                if stack and stack[-1]==map1[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

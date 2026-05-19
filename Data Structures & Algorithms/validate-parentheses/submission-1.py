class Solution:
    def isValid(self, s: str) -> bool:
        reverseMap = {"}": "{", ")": "(", "]": "["}
        stack=[]
        for i in range(len(s)):
            if s[i] in reverseMap:
                if stack:
                    val = stack.pop()
                    if reverseMap[s[i]] != val:
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
        return not stack
                
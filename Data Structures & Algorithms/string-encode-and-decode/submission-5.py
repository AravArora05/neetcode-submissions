class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode and decode strings
        #you can't add strings and numbers together
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        an = []
        while i < len(s):
            #okay, so you'll be traversing with a for loop
            number = ""
            j = i
            while s[j] != "#":
                number += s[j]
                j+=1 
            #so once number = i, that's when it matters
            number = int(number)
            word = s[j + 1: j + 1 + number]
            an.append(word)
            i = j + 1 + number
        return an

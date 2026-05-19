class Solution:
    #encode and decode strings, neccesary to do for both
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += str(len(word)) + "#" + word
        return ans

    def decode(self, s: str) -> List[str]:
            i = 0
            list1 = []
            while i < len(s):
                #so seeing if i < len(s)
                number = ""
                j = i
                while s[j] != "#":
                    number += s[j]
                    j += 1
                #okay so now we've got the word
                number = int(number)
                word = s[j + 1: j + 1 + number]
                list1.append(word)
                i = j + 1 + number
            return list1
class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word))+ "#" + word
        return string



    def decode(self, s: str) -> List[str]:
        i = 0
        arr = []
        while i < len(s):
            curr = ""
            while s[i] != "#":
                curr += s[i]
                i += 1
            #now you've got to s
            number = int(curr)
            arr.append(s[i + 1: i + 1 + number])
            i = i + 1 + number
        return arr
                

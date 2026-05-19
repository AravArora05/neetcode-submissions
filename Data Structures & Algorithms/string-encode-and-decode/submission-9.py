class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string+=str(len(word))
            string+="#"
            string+=word
        return string

    def decode(self, s: str) -> List[str]:
        i, res = 0, []
        while i < len(s):
            j = i+1
            while s[j] != "#":
                j+=1
            value = int(s[i:j])
            res.append(s[j + 1: j + 1 + value])
            i = j + 1 + value
        return res
            

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans


    def decode(self, s: str) -> List[str]:
        list1 = []
        i = 0
        while i < len(s):
            j = i
            while (s[j] != "#"):
                j+= 1
            length = int(s[i: j])
            list1.append(s[j + 1: j + 1 + length])
            i = j + length + 1
        return list1                
        

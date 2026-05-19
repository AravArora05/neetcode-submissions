class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1=defaultdict(int)
        map2=defaultdict(int)
        l=0
        if len(s)!=len(t):
            return False
        while l<len(s):
            map1[s[l]]+=1
            map2[t[l]]+=1
            l+=1
        return map1==map2
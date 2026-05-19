class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #given two strings
        #return true if the two strings are anagrams
        #else return false
        freq1=defaultdict(int)
        freq2=defaultdict(int)
        if len(t) != len(s):
            return False
        #we want arrays to map the frequence of each character
        for i, char in enumerate(s):
            freq1[char]+=1
            freq2[t[i]]+=1
        return freq1==freq2
            
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] +=1
            map1[tuple(counts)].append(word)
        return list(map1.values())

        
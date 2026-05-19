class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)
        for word in strs:
            #go through each word
            array=[0] * 26
            for char in word:
                array[ord(char)-ord("a")]+=1
            map1[tuple(array)].append(word)
        return list(map1.values())

                
                
        
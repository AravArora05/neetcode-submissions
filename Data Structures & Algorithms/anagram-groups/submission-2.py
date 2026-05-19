class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #you want to iterate through each word
        #essentially have the array w/ frequency being the key
        #value is technically a tuple(but limk tuple of everything)
        hashmap=defaultdict(list)
        for word in strs:
            array=[0]*26
            for char in word:
                array[ord(char)-ord("a")]+=1
            hashmap[tuple(array)].append(word)
        return list(hashmap.values())
        
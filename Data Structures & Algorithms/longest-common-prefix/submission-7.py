class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comm_ind=0
        #you want to iterate through each word
        shortest=min(len(word) for word in strs)
        for i in range(shortest):
            curr_char='a'
            for j, word in enumerate(strs):
                if j==0:
                    curr_char=word[i]
                else:
                    if word[i]!=curr_char:
                        return strs[0][0: comm_ind]
            comm_ind+=1
        return strs[0][0:comm_ind]
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #okay number of connected components
        par = [i for i in range(n)]
        rank = [1] * n
        #you want an array for N's
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] == par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            #okay, so you're doing the union of the two nodes
            #n1 and n2
            pear = find(n1)
            apple = find(n2)
            if pear == apple:
                return 0
            #you don't want to add them together if they've got the same parent
            if rank[pear] > rank[apple]:
                rank[pear] += rank[apple]
                par[apple] = par[pear]
            else:
                rank[apple] += rank[pear]
                par[pear] = par[apple]
            return 1
        
        for p1, p2 in edges:
            n -= union(p1, p2)
        return n
                #okay so it has a new parent

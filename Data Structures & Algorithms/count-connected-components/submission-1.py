class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        #okay, so you have these two values
        count = n

        def find(node):
            res = node
            while (par[res] != res):
                par[res] = par[par[res]]
                res = par[res]
            return res

            
        def union(n1, n2):
            par1, par2 = find(n1), find(n2)
            if (par1 == par2):
                return 0
            else:
                if (rank[par1] > rank[par2]):
                    par[par2] = par1
                    rank[par1] += rank[par2]
                else:
                    par[par1] = par2
                    rank[par2] += rank[par1]
            return 1

        for n1, n2 in edges:
            count -= union(n1, n2)
        return count

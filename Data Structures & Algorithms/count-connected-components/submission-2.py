class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = n
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while (par[res] != res):
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            #so you're going to hav eto find both of these nodes and their fellow
            if p1 == p2:
                return 0
                #there's ntohing to do
            else:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]
            return 1
        for n1, n2 in edges:
            count -= union(n1, n2)
        return count
        
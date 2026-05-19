class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        adjmap = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjmap[n1].append(n2)
            adjmap[n2].append(n1)
            #you're adding both values

        def dfs(val, prev):
            if val in visit:       
                return False
            visit.add(val)
            for adj in adjmap[val]:
                if adj == prev:
                    continue
                if not dfs(adj, val):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
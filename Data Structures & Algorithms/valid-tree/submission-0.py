class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
            #you've got the best of both worlds

        visit = set()
        def dfs(val, prev):
            if val in visit:
                return False
            visit.add(val)
            for adj in adjList[val]:
                if (prev == adj):
                    continue
                if not dfs(adj, val):
                    return False
            return True
        return dfs(0, - 1) and len(visit) == n
            
    
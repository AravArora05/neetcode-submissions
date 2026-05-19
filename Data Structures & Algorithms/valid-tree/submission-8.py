class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #def Valid Tree
        #you've got n the number of edges
        #you have the adjaency lizst and must do it 
        if not edges:
            return True

        adjList = {}
        for st, ed in edges:
            if st not in adjList:
                adjList[st] = []
            if ed not in adjList:
                adjList[ed] = []
            adjList[st].append(ed)
            adjList[ed].append(st)

        visit = set()
        def dfs(value, prev):
            if value in visit:
                return False
            visit.add(value)
            for neighbor in adjList[value]:
                if prev == neighbor:
                    continue
            #traverse through each of the neighbors
                if not dfs(neighbor, value):
                    return False
            return True
        
        return dfs(edges[0][0], -1) and len(visit) == n
        #you want you're prev to be -1 becayuse you might not see it before
        
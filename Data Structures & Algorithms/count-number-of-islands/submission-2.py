class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        def dfs(r,c):
            if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in visit or grid[r][c]=="0":
                return
            visit.add((r,c))
            dfs(r-1,c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return
        count=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visit and grid[row][col]=="1":
                    count+=1
                    dfs(row,col)
        return count
                    
        
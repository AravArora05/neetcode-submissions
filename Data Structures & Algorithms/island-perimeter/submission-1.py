class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #island doesn't have laks
        #water inside isn't connect to water around island
        visit=set()
        def dfs(r, c):
            if (r,c) in visit:
                return 0
            if r not in range(len(grid)) or c not in range(len(grid[0])) or grid[r][c]==0:
                return 1
            visit.add((r,c))
            left=dfs(r-1,c)
            right=dfs(r+1,c)
            top=dfs(r,c-1)
            bottom=dfs(r, c+1)
            return left + right + top + bottom
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    return dfs(row,col)        
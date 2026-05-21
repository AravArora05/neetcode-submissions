class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        def dfs(r, c):
            if (r,c) in visit or r not in range(len(grid)) or c not in range(len(grid[0])) or grid[r][c]==0:
                return 0
            visit.add((r,c))
            return 1 + dfs(r-1,c)+dfs(r+1,c)+dfs(r, c+1)+dfs(r,c-1)
            #so you have the dfs and everything they account for
        max_area=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1 and (row, col) not in visit:
                    val=dfs(row, col)
                    max_area=max(max_area, val)
        return max_area
                    
            
        
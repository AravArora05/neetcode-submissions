class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #walls and gates, a very difficulit leet code problem
        queue = deque()
        visit = set()

        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 0):
                    queue.append((r, c))
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == 2147483647:
                    grid[r][c] = dist
                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c -1)]
                for dr, dc in neighbors:
                    if (dr in range(rows) and dc in range(cols) and (dr, dc) not in visit and grid[dr][dc] == 2147483647):
                        visit.add((dr, dc))
                        queue.append((dr, dc))
            dist += 1
        return grid


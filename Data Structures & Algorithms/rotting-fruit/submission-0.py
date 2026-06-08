class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh+=1 

        dirns = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        ctr = 0
        while fresh and q:
            ctr += 1
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                
                for dr, dc in dirns:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols) and grid[row][col]==1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
        
        return ctr if not fresh else -1 
                
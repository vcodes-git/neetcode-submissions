class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # TODO: 
        # fucn for sinking island

        dirns = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def sinkDFS(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            for dirn in dirns:
                sinkDFS(r + dirn[0], c + dirn[1])



        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    sinkDFS(r, c)
                    islands += 1

        return islands

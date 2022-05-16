class Solution:
    # outer loop: O(n); inner loop: O(1) as max 8 directions
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        queue = [[0, 0]]
        grid[0][0] = 1
        
        while len(queue) != 0:
            path = queue.pop(0)
            value = grid[path[0]][path[1]]
            if path[0] == len(grid) - 1 and path[1] == len(grid[0]) - 1:
                return value
            
            result = self.getAdjacent(path, grid)
            for r in result:
                row, col = r
                grid[row][col] = value + 1
                queue.append([row, col])
            
        return -1
        
    def getAdjacent(self, path: List[int], grid: List[List[int]]) -> List[List[int]]:
        result = []
        r, c = path
        
        if r > 0:
            if grid[r - 1][c] == 0:
                result.append([r - 1, c])

        if c > 0:
            if grid[r][c - 1] == 0:
                result.append([r, c - 1])

        if r + 1 <= len(grid) - 1:
            if grid[r + 1][c] == 0:
                result.append([r + 1, c])

        if c + 1 <= len(grid[0]) - 1:
            if grid[r][c + 1] == 0:
                result.append([r, c + 1])

        if r > 0 and c > 0:
            if grid[r - 1][c - 1] == 0:
                result.append([r - 1, c - 1])

        if r > 0 and c + 1 <= len(grid[0]) - 1:
            if grid[r - 1][c + 1] == 0:
                result.append([r - 1, c + 1])

        if r + 1 <= len(grid) - 1 and c > 0:
            if grid[r + 1][c - 1] == 0:
                result.append([r + 1, c - 1])

        if r + 1 <= len(grid) - 1 and c + 1 <= len(grid[0]) - 1:
            if grid[r + 1][c + 1] == 0:
                result.append([r + 1, c + 1])
        
        return result
            
        

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # maintain a queue for bfs
        numRows = len(mat)
        numCols = len(mat[0])
        # initialize output with largest distances
        output = [[numCols * numRows] * numCols for i in range(numRows)]
        q = []
        
        # find all zeros and add them to the queue
        for i in range(numRows):
            for j in range(numCols):
                if mat[i][j] == 0:
                    output[i][j] = 0
                    q.append([i, j])
        
        # pop the cell from queue and examine its neighbors
        # if the calculated distance is smaller then update
        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        while q:
            curr = q.pop(0)
            for i in range(len(direction)):
                r = curr[0] + direction[i][0]
                c = curr[1] + direction[i][1]
                if r >= 0 and c >= 0 and r < numRows and c < numCols:
                    if output[r][c] > output[curr[0]][curr[1]] + 1:
                        output[r][c] = output[curr[0]][curr[1]] + 1
                        q.append([r, c])
        
        return output

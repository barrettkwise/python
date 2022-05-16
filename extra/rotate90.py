class RotateList:
    def rotate(matrix):
        RotateList.transpose(matrix)
        RotateList.reflect(matrix)
        return matrix
    
    def transpose(matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


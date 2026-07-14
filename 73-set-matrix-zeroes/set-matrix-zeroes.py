class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        frz=False
        fcz=False

        for i in range(col):
            if matrix[0][i]==0:
                fcz=True
                break
        for i in range(row):
            if matrix[i][0]==0:
                frz=True
                break
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if frz:
            for i in range(row):
                matrix[i][0]=0
        if fcz:
            for j in range(col):
                matrix[0][j]=0
        return matrix


        
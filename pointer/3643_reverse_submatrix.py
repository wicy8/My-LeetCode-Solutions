from typing import List

class Solution:
    def reverseSubmatrix(self,grid:List[List[int]],x:int,y:int,k:int)->List[List[int]]:
        """
        思路：从（x,y）处开始，依次遍历grid，
            对grid[x+i][y+j]和grid[x+k-i][y+j]进行交换
        """
        # for i in range(k):
        #     for j in range(k//2):
        #         grid[x + j][y+i],grid[x+k-j-1][y+i]=grid[x+k-j-1][y+i],grid[x + j][y+i]
        # return grid

        for j in range(k//2):
            grid[x + j][y:y+k],grid[x+k-j-1][y:y+k]=grid[x+k-j-1][y:y+k],grid[x + j][y:y+k]
        return grid

if __name__=="__main__":
    s=Solution()
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    x = 1
    y = 0
    k = 3
    print(s.reverseSubmatrix(grid,x,y,k))

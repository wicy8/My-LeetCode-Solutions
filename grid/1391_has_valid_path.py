from typing import List

class Solution:
    def hasValidPath(self,grid:List[List[int]])->bool:
        """
        思路：for循环m*n次，每次移动一格，记录移动的方向7890左上右下，
            如果当前方向是上，下一个小格子不接受上（下左右），则返回False
            for循环结束或i=m-1 and j=n-1返回True
        思路2：使用dfs
        """
        m=len(grid)
        n=len(grid[0])
        k=1
        flag=False
        if m*n==1:
            return True
        if grid[0][0]==1:
            di=9
        elif grid[0][0]==2:
            di=0
        elif grid[0][0]==3:
            di=0
        elif grid[0][0]==4:
            di=9
            k=2
        elif grid[0][0] ==5:
            return False
        else:
            di=9
        i=0
        j=0
        for _ in range(k):
            for _ in range(m*n):
                if di==8 or di==0:
                    i+=-1 if di==8 else 1
                elif di==7 or di==9:
                    j+=-1 if di==7 else 1
                if i < 0 or i >= m or j < 0 or j >= n:
                    break
                v = grid[i][j]
                if di==7:
                    if v==1:
                        pass
                    elif v==4:
                        di=0
                    elif v==6:
                        di=9
                    else:
                        break
                elif di==8:
                    if v==2:
                        pass
                    elif v==3:
                        di=7
                    elif v==4:
                        di=9
                    else:
                        break
                elif di==9:
                    if v==1:
                        pass
                    elif v==3:
                        di=0
                    elif v==5:
                        di=8
                    else:
                        break
                else:
                    if v==2:
                        pass
                    elif v==5:
                        di=7
                    elif v==6:
                        di=9
                    else:
                        break
                if i==m-1 and j==n-1:
                    return True
            di=0
            i,j=0,0
        return flag


if __name__=="__main__":
    s=Solution()
    grid = [[2],[6]]
    print(s.hasValidPath(grid))

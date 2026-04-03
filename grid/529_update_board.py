from typing import List

class Solution:
    def updateBoard(self,board:List[List[str]],click:List[int])->List[List[str]]:
        """
        思路：判断click是否是M，如果是M，将M改成X返回
            如果不是M，使用DFS遍历，附近有雷则停止DFS返回到上个点，
            如果没雷，继续遍历
        """
        r,c=click
        if board[r][c]=='M':
            board[r][c]='X'
            return board
        m,n=len(board),len(board[0])
        def dfs(i,j):
            cnt=0
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if 0<=x<m and 0<=y<n and not (x==i and y==j) and board[x][y]=='M':
                        cnt+=1
            if cnt>0:
                board[i][j]=str(cnt)
                return
            board[i][j]='B'
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if 0<=x<m and 0<=y<n and not (x==i and y==j) and board[x][y]=='E':
                        dfs(x,y)
            return
        dfs(r,c)
        return board

if __name__=="__main__":
    s=Solution()
    board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"],
             ["E", "E", "E", "E", "E"]]
    click = [3, 0]
    print(s.updateBoard(board,click))
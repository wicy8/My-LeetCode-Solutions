from typing import List

class Solution:
    def spiralMatrixIII(self,rows:int,cols:int,rStart:int,cStart:int)->List[List[int]]:
        """
        思路：创建一个数组记录转弯方向，每次循环向前走n步，
            每循环一次变换一次方向，每循环两次n+1，
            直到ans的长度为r*c
        """
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        a=0
        n=1
        x=rStart
        y=cStart
        i=0
        ans=[[rStart,cStart]]
        while len(ans)<rows*cols:
            for _ in range(n):
                x+=dir[a][0]
                y+=dir[a][1]
                if 0<=x<rows and 0<=y<cols:
                    ans.append([x,y])
                if not 0<=x<rows and (a==0 or a==2):
                    x+=dir[a][0]*(n-1)
                    y+=dir[a][1]*(n-1)
                    break
                elif not 0<=y<cols and (a==1 or a==3):
                    x += dir[a][0] * (n - 1)
                    y += dir[a][1] * (n - 1)
                    break
            a=(a+1)%4
            i+=1
            if i%2==0 and i!=0:
                n+=1
        return ans

if __name__=="__main__":
    s=Solution()
    rows = 5
    cols = 6
    rStart = 1
    cStart = 4
    print(s.spiralMatrixIII(rows,cols,rStart,cStart))


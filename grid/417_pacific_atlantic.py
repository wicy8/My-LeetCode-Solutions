from typing import List

class Solution:
    def pacificAtlantic(self,heights:List[List[int]])->List[List[int]]:
        """
        思路1：对heights进行遍历，对每个元素进行DFS遍历，判断是否能到达两个海洋，
            如果不能则将他遍历过的元素设置为已遍历
        思路2：从边缘开始DFS遍历，左上侧的元素遍历一次，右下侧的元素遍历一次，取两者交集
        """
        # m,n=len(heights),len(heights[0])
        # flag=[[0]*n for _ in range(m)]
        # results=[]
        # def dfs(i,j):
        #     po=0#是否能到太平洋
        #     ao=0#是否能到大西洋
        #     flag[i][j]=1
        #     if i==0 or j==0:
        #         po=1
        #     if i==m-1 or j==n-1:
        #         ao=1
        #     for x,y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        #         if 0<=x<m and 0<=y<n and flag[x][y]==0 and heights[x][y]<=heights[i][j]:
        #             p,a=dfs(x,y)
        #             po+=p
        #             ao+=a
        #     return po,ao
        # for i in range(m):
        #     for j in range(n):
        #         flag = [[0] * n for _ in range(m)]
        #         po,ao=dfs(i,j)
        #         if po>0 and ao>0:
        #             results.append([i,j])
        # return results

        m,n=len(heights),len(heights[0])
        results=set()
        vis=set()
        def dfs(i,j):
            if (i,j) in vis:
                return
            vis.add((i,j))
            for x,y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0<=x<m and 0<=y<n and (x,y) not in vis and heights[x][y]>=heights[i][j]:
                    dfs(x,y)
        for i in range(max(m,n)):
            dfs(0,i) if i<n else None
            dfs(i,0) if i<m else None
        results=vis
        vis=set()
        for i in range(max(m,n)):
            dfs(m-1,i) if i<n else None
            dfs(i,n-1) if i<m else None
        return list((results & vis))

if __name__=="__main__":
    s=Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(s.pacificAtlantic(heights))


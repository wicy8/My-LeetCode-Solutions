from typing import List

class Solution:
    def robotSim(self,commands:List[int],obstacles:List[List[int]])->int:
        """
        思路：初始化一个列表dir记录每个方向的坐标加减值，
            每次转向都获取一次dir[a]的值，其中a=a%4
            根据方向、距离和障碍控制机器人的行走，
            最后对坐标进行平方相加得结果
        思路2：前面不变，将obstacles转成哈希表
            判断坐标是否在哈希表中，如果不在则可以增加
            否则中断
        """
        # dir=[(0,1),(1,0),(0,-1),(-1,0)]
        # a=0
        # x,y=0,0
        # ans=0
        # obstacles
        # for c in commands:
        #     if c<0:
        #         if c==-1:
        #             a+=1
        #             a=a%4
        #         elif c==-2:
        #             a-=1
        #             a=a%4
        #         else:
        #             continue
        #     elif 1<=c<=9:
        #         t=c
        #         if a==0:
        #             for obstacle in obstacles:
        #                 if obstacle[0]==x and y<obstacle[1]<=y+c:
        #                     t=min(obstacle[1]-y-1,t)
        #         elif a==1:
        #             for obstacle in obstacles:
        #                 if obstacle[1]==y and x<obstacle[0]<=x+c:
        #                     t=min(obstacle[0]-x-1,t)
        #         elif a==2:
        #             for obstacle in obstacles:
        #                 if obstacle[0]==x and y-c<=obstacle[1]<y:
        #                     t=min(y-obstacle[1]-1,t)
        #         elif a==3:
        #             for obstacle in obstacles:
        #                 if obstacle[1]==y and x-c<=obstacle[0]<x:
        #                     t=min(x-obstacle[0]-1,t)
        #         x+=t*dir[a][0]
        #         y+=t*dir[a][1]
        #     else:
        #         continue
        #     ans=max(x**2+y**2,ans)
        # return ans

        obstacle_set = set(map(tuple, obstacles))
        ans = x = y = k = 0
        DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)
        for c in commands:
            if c == -1:  # 右转
                k = (k + 1) % 4
            elif c == -2:  # 左转
                k = (k - 1) % 4
            else:  # 直行
                while c > 0 and (x + DIRS[k][0], y + DIRS[k][1]) not in obstacle_set:
                    x += DIRS[k][0]
                    y += DIRS[k][1]
                    c -= 1
                ans = max(ans, x * x + y * y)
        return ans

if __name__=="__main__":
    s=Solution()
    commands = [7,-2,-2,7,5]
    obstacles = [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]]
    print(s.robotSim(commands,obstacles))
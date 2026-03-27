from typing import List

class Solution:
    def asteroidCollision(self,asteroids:List[int])->List[int]:
        """
        思路1：当正遇到负时，绝对值小的元素设为0，最后把0元素剔除。
        思路2：使用栈，当遇到正数时入栈，否则比较，正数小出栈。
        """
        # n=len(asteroids)
        # i=0
        # j=-1#记录遍历过的，最靠左的正数位置
        # k=-1#记录遍历过的，最靠右的正数位置
        # while i<n:
        #     if asteroids[i]>0:
        #         j=i if j==-1 else j
        #         k=i
        #         i+=1
        #         continue
        #     elif asteroids[i]<0 and k>=j>=0:
        #         while abs(asteroids[i])>=asteroids[k] and k>=j>=0:
        #             asteroids[i]=0 if abs(asteroids[i])==asteroids[k] else asteroids[i]
        #             asteroids[k]=0
        #             while asteroids[k]<=0:
        #                 k-=1
        #                 if k<j:
        #                     j=-1
        #                     break
        #         if abs(asteroids[i])<asteroids[k]:
        #             asteroids[i]=0
        #         i+=1
        #     else:
        #         i+=1
        # asteroids=[x for x in asteroids if x!=0]
        # return asteroids

        a=[]
        for x in asteroids:
            if x>0:
                a.append(x)
            elif x<0 and len(a)>0 and a[-1]>0:
                while abs(x)>a[-1]:
                    a.pop(-1)
                    if len(a)==0 or a[-1]<0:
                        a.append(x)
                        break
                if abs(x)==a[-1]:
                    a.pop(-1)
            else:
                a.append(x)
        return a



if __name__=="__main__":
    s=Solution()
    asteroids = [[5, 10, -5],[8,-8],[10,2,-5],[3,5,-6,2,-1,4],[-2,-1,1,2]]
    print(s.asteroidCollision(asteroids[3]))

from typing import List


class Solution:
    def findPoisonedDuration(self,timeSeries: List[int],duration: int) -> int:
        """
        思路：获取两次攻击间隔与持续时间的最小值，即本次攻击间隔内的中毒时间。
        """
        ans=0
        length = len(timeSeries)
        for i in range(length-1):
            ans+=min(timeSeries[i+1]-timeSeries[i],duration)
        ans+=duration
        return ans

if __name__=='__main__':
    s=Solution()
    timeSeries=[1,2]
    duration=2
    print(s.findPoisonedDuration(timeSeries,duration))
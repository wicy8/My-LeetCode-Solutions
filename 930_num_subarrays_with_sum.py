from typing import List


class Solution:
    def numSubarraysWithSum(self, nums:List[int],goal:int)->int:
        """
        思路：恰好n个子数组问题，可以转换为求两个至少k个子数组减去至少k+1个子数组问题
            封装一个函数，求两次至少子数组问题
        至少子数组问题：遍历nums，统计加和cnt，若等于goal，则缩小窗口
            ans+=left
        """
        def solve(nums,goal):
            ans = 0
            left = 0
            cnt = 0
            for i,x in enumerate(nums):
                cnt+=x
                while cnt >= goal and left<=i:
                    cnt -= nums[left]
                    left += 1
                ans += left
            return ans

        return solve(nums,goal)-solve(nums,goal+1)

if __name__=='__main__':
    nums=[0,0,0,0,0]
    goal=0
    s = Solution()
    print(s.numSubarraysWithSum(nums,goal))

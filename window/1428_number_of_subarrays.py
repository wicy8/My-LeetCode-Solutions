from typing import List


class Solution:
    def sumOfSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        题目：给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
            请返回这个数组中 「优美子数组」 的数目。
        思路：遍历nums，记录子数组中奇数的个数cnt，返回cnt大于k的子数组个数减去cnt大于等于k的子数组个数。
        """
        ans=0
        l1,l2=0,0
        cnt1,cnt2=0,0
        for i,x in enumerate(nums):
            t=1 if x%2==1 else 0
            cnt1+=t
            cnt2+=t
            while cnt1>=k:
                cnt1-=1 if nums[l1]%2==1 else 0
                l1+=1
            while cnt2>k:
                cnt2 -= 1 if nums[l2] % 2 == 1 else 0
                l2 += 1
            ans += l1-l2
        return ans

if __name__=='__main__':
    s = Solution()
    print(s.sumOfSubarrays([2,4,6],1))
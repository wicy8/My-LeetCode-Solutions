from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        思路：遍历nums，使用字典记录的元素的个数，和满足条件的个数cnt=a[x]-1，
        如果cnt等于k，则缩小窗口，另ans+=left
        """
        ans = 0
        left = 0
        a = defaultdict(int)
        cnt = 0
        for i, x in enumerate(nums):
            a[x] += 1
            cnt += a[x] - 1
            while cnt >= k:
                a[nums[left]] -= 1
                cnt -= a[nums[left]]
                left += 1
            ans += left
        return ans

if __name__ == '__main__':
    s=Solution()
    print(s.countGood([1,1,1,1,1],10))
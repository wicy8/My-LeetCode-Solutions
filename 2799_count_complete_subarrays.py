from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> List[int]:
        """
        思路：遍历nums，使用哈希表记录元素，如果哈希表长度等于nums不同元素个数，
        则缩小窗口，ans+=left
        为什么：left之前都是满足条件的子数组
        """
        ans = 0
        left = 0
        a = defaultdict(int)
        cnt = len(set(nums))  # 统计nums不同元素个数
        for x in nums:
            a[x] += 1
            while len(a) == cnt:
                a[nums[left]] -= 1
                if a[nums[left]] == 0:
                    del a[nums[left]]
                left += 1
            ans += left
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countCompleteSubarrays([1,3,1,2,2]))
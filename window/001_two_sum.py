from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        题目：两数之和
        思路：使用哈希表 (HashMap) 存储遍历过的数字，实现 O(n) 时间复杂度。
        """
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in nums and i != hashMap[target - nums[i]]:
                return [i, hashMap[target - nums[i]]]

if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))
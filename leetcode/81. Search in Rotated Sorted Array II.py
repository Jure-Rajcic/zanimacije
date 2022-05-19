from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i = 0
        if target > nums[0]:
            while i < len(nums) and nums[i] < target:
                i = i + 1
        else:
            while i < len(nums) and target != nums[i]:
                i = i + 1
        if i == len(nums):
            return False
        return target == nums[i]

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,2,3,2,2,2]
    print(s.search(nums, 3))
    nums = [2,5,6,0,0,1,2]
    print(s.search(nums, 0))
    nums = [5, 1, 3]
    print(s.search(nums, 3))


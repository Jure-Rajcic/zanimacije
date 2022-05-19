from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = [0] * (len(nums) - 1)
        for i in range(0, len(nums)):
            index = nums[i] - 1
            if x[index] == 1:
                return index + 1
            else:
                x[index] = 1

if __name__ == '__main__':
    nums = [1,1,2]
    s = Solution()
    print(s.findDuplicate(nums))
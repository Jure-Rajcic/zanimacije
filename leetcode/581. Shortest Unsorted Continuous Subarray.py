from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        x = len(nums)
        y = 0
        while y < len(nums) and nums[y] == sorted_nums[y]:
            y +=1
            x -=1

        if y < len(nums):
            y = len(nums) - 1
            while y >= 0 and nums[y] == sorted_nums[y]:
                y -=1
                x-=1
        return x



if __name__ == '__main__':
    s = Solution()
    a = s.findUnsortedSubarray([2,6,4,8,10,9,15])
    print(a)
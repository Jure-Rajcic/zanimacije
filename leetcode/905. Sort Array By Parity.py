from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            while nums[l] & 0x1 == 0 and l < r:
                l += 1
            while nums[r] & 0x1 == 1 and l < r:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(3 // 2)
    print(s.sortArrayByParity([0, 2]))
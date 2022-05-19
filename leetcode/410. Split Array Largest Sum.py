from typing import List


class Solution:
    def canSplit(self, largest):
        subarray = 0
        curSum = 0
        for n in nums:
            curSum += n
            if curSum > largest:
                subarray += 1
                curSum = n
        return subarray + 1 <= m


    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if self.canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    s = Solution()
    print(s.splitArray(nums, m))
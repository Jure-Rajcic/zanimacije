class Solution:

    def R(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return self.R(s, start + 1, end) or self.R(s, start, end - 1)
            start+=1
            end-=1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("abc"))
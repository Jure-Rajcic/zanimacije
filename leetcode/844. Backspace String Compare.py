class Solution:

    def x(self, s: str) -> str:
        s2 = ""
        for i in range(0, len(s)):
            if s[i] == '#':
                if s == "":
                    continue
                else:
                    s2 = s2[0: len(s2) - 1]
            else:
                s2 = s2 + s[i]

        return s2

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.x(s) == self.x(t)


if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare("ab#c", "ad#c"))
    print(s.backspaceCompare("ab##", "c#d#"))
    print(s.backspaceCompare("a#c", "d"))

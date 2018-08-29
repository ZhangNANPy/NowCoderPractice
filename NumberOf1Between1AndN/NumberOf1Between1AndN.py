# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        sn = str(n)
        l = len(sn)
        if l == 1:
            if n < 1:
                return 0
            else:
                return 1
        snum = n % (10 ** (l - 1))
        bnum = n - snum
        card = 1
        n1 = 0
        while bnum // (card * 10) > 0:
            n1 = n1 + bnum // (card * 10) * card
            card = card * 10
        if bnum // card > 1:
            return n1 + card + self.NumberOf1Between1AndN_Solution(snum)
        else:
            return n1 + self.NumberOf1Between1AndN_Solution(snum) + snum + 1


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution(21345))


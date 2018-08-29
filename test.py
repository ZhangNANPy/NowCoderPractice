# -*- coding:utf-8 -*-
class Solution:
    def array_num(self, l, r):
        count = 0
        num = 0
        for i in range(l):
            num = num + sum([int(j) for j in str(i)])
        for i in range(l, r + 1):
            num = num + sum([int(j) for j in str(i)])
            if num % 3 == 0:
                count = count + 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.array_num(2,5))
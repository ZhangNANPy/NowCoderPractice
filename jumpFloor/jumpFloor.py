# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        return self.Fibonacci(number + 1)

    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        f0 = 0
        f1 = 1
        for i in range(2, n + 1):
            f0 = f0 + f1
            f0, f1 = f1, f0
        return f1
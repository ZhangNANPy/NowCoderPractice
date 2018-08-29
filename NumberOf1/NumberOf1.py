# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        strn = bin(n)
        counter = 0
        if strn[0] == '-':
            i = len(strn) - 1
            strf = []
            while strn[i] != 'b':
                if strn[i] == '0':
                    strf.append('1')
                elif strn[i] == '1':
                    strf.append('0')
                i = i - 1
            while len(strf) < 32:
                strf.append('1')
            for i in range(len(strf)):
                if strf[i] == '1':
                    strf[i] = '0'
                elif strf[i] == '0':
                    strf[i] = '1'
                    break
            if strf[-1] == '0':
                strf.append('1')
            strn = strf
        for i in strn:
            if i == '1':
                counter = counter + 1
        return counter

if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(-2))
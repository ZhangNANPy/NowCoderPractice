# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # begin = 0
        # end = len(array) - 1
        # while end - begin > 1:
        #     while array[begin] % 2 != 0:
        #         begin = begin + 1
        #     while array[end] % 2 != 1:
        #         end = end -1
        #     array[begin], array[end] = array[end], array[begin]
        # return array
        odd = []
        i = 0
        while i < len(array):
            if array[i] % 2 == 1:
                odd.append(array[i])
                del array[i]
            else:
                i = i + 1
        return odd + array

if __name__ == '__main__':
    s = Solution()
    print(s.reOrderArray([2,4,6,1,3,5,7]))
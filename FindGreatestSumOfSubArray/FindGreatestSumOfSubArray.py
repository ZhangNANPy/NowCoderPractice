# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        array_max = array[0]
        temp = 0
        for right in range(0, len(array)):
            temp = temp + array[right]
            if temp > array_max:
                array_max = temp
            if temp < 0:
                temp = 0
        return array_max
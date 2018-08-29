# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        left = 0
        up = 0
        down = len(matrix)
        right = len(matrix[0])
        re = []
        while left < right and up < down:
            re = re + (matrix[up][left:right])
            if down - up > 1:
                for i in range(up+1, down):
                    re.append(matrix[i][right-1])
                if right - left > 1:
                    temp = matrix[down-1][left:right-1]
                    temp.reverse()
                    re = re + temp
                    for i in range(down-2, up, -1):
                        re.append(matrix[i][left])
            left = left + 1
            right = right - 1
            up = up + 1
            down = down - 1
        return re


if __name__ == '__main__':
    s = Solution()
    m = [[1,2],[3,4]]
    print(s.printMatrix(m))


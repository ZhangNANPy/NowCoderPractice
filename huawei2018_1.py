# -*- coding:utf-8 -*-
'''给定一个数组是每天股票的价格，输出最大获利。
示例：2Y 3S 4S 6Y 8S
输出：76'''

s = []
s = input().split()
m = []
for i in s:
    if i[-1].lower() == 's':
        k = int(i[:-1]) * 7
    else:
        k = int(i[:-1])
    m.append(k)


def profit(prices):
    if len(prices) < 2:
        return 0
    p = 0
    for i in range(1, len(prices)):
            p = p + max(0, prices[i] - prices[i - 1])
    return p


if __name__ == '__main__':
    print(profit(m))


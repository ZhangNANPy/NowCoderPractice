# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.empty = myStack()
        self.data = myStack()

    def push(self, node):
        self.data.push(node)

    def pop(self):
        t = self.data.pop()
        while t is not None:
            self.empty.push(t)
            t = self.data.pop()
        r = self.empty.pop()
        t = self.empty.pop()
        while t is not None:
            self.data.push(t)
            t = self.empty.pop()
        return r


class myStack:
    def __init__(self):
        self.stack = []

    def push(self, node):
        self.stack.append(node)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            t = self.stack[-1]
            del self.stack[-1]
            return t

if __name__ == '__main__':
    q = Solution()
    q.push(4)
    print(q.pop())


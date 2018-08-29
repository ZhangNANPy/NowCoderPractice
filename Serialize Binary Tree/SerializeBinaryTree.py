# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self, l=512):
        self.ltn = [1]
        self.rtn = []
        lr = 0
        while self.ltn[lr] * 2 + 2 < l:
            self.ltn.append(self.ltn[lr] * 2 + 1)
            self.ltn.append(self.ltn[lr] * 2 + 2)
            lr = lr + 1
        if self.ltn[lr] * 2 + 1 < l:
            self.ltn.append(self.ltn[lr] * 2 + 1)
        for i in range(2, 512):
            if i not in self.ltn:
                self.rtn.append(i)

    def Serialize(self, root):
        if not root:
            return []
        re = []
        tl = [root]
        dl = []
        while tl:
            for i in tl:
                if i:
                    re.append(i.val)
                    dl.append(i.left)
                    dl.append(i.right)
                else:
                    re.append(None)
                    dl.append(None)
                    dl.append(None)
            tl = dl
            dl = []
            flag = False
            for i in tl:
                if i:
                    flag = True
                    break
            if flag:
                continue
            else:
                break
        return re

    def Deserialize(self, s):
        if not s or not s[0]:
            return None
        if len(s) == 1 and s[0]:
            return TreeNode(s[0])
        root = TreeNode(s[0])
        lts = []
        rts = []
        i = 0
        while self.ltn[i] < len(s):
            lts.append(s[self.ltn[i]])
            i = i + 1
        i = 0
        while self.rtn[i] < len(s):
            rts.append(s[self.rtn[i]])
            i = i + 1
        root.left = self.Deserialize(lts)
        root.right = self.Deserialize(rts)
        return root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = None
    root.left.left = TreeNode(3)
    root.left.right = None
    # root.right.left = TreeNode(2)
    # root.right.right = TreeNode(11)
    s = Solution()
    print(s.Serialize(root))
    print(s.Serialize(s.Deserialize(s.Serialize(root))))


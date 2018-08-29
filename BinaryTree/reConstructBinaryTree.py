# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        tn = TreeNode(pre[0])
        if len(pre) == 1:
            return tn
        i = tin.index(pre[0])
        if i == 0:
            rtin = tin[i + 1:]
            rpre = pre[i + 1:]
            tn.right = self.reConstructBinaryTree(rpre, rtin)
        elif i == len(tin) - 1:
            ltin = tin[0:i]
            lpre = pre[1:i + 1]
            tn.left = self.reConstructBinaryTree(lpre, ltin)
        else:
            ltin = tin[0:i]
            rtin = tin[i+1:]
            lpre = pre[1:i+1]
            rpre = pre[i+1:]
            tn.left = self.reConstructBinaryTree(lpre, ltin)
            tn.right = self.reConstructBinaryTree(rpre, rtin)
        return tn


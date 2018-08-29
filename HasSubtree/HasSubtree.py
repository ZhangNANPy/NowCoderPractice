# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val == pRoot2.val:
            if pRoot2.left == None and pRoot2.right == None:
                return True
            elif pRoot2.left != None and pRoot2.right == None:
                return self.HasSubtree(pRoot1.left, pRoot2.left) or self.HasSubtree(pRoot1.left, pRoot2)
            elif pRoot2.left == None and pRoot2.right != None:
                return self.HasSubtree(pRoot1.right, pRoot2.right) or self.HasSubtree(pRoot1.right, pRoot2)
            elif pRoot2.left != None and pRoot2.right != None:
                return (self.HasSubtree(pRoot1.left, pRoot2.left) and self.HasSubtree(pRoot1.right, pRoot2.right)) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)


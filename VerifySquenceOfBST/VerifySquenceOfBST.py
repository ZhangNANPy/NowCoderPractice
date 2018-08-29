# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 1:
            return True
        elif not sequence:
            return False
        root = sequence.pop()
        left_tree_sequence = []
        right_tree_sequence = []
        i = 0
        for i in range(len(sequence)):
            if sequence[i] < root:
                left_tree_sequence.append(sequence[i])
            else:
                right_tree_sequence = sequence[i:]
                break
        for i in right_tree_sequence:
            if root > i:
                return False
        if left_tree_sequence and right_tree_sequence:
            return self.VerifySquenceOfBST(left_tree_sequence) and self.VerifySquenceOfBST(right_tree_sequence)
        elif left_tree_sequence:
            return self.VerifySquenceOfBST(left_tree_sequence)
        else:
            return self.VerifySquenceOfBST(right_tree_sequence)


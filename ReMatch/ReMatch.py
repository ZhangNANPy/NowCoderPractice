# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if not s:
            if not pattern:
                return True
            elif len(pattern) == 2 and pattern[1] == '*':
                return True
        elif not pattern:
            return False
        if pattern[0] == '*':
            return False
        pattern_list = []
        l = 0
        for i in range(len(pattern)):
            if pattern[i] == '.':
                pattern_list.append(pattern[i-l:i])
                pattern_list.append('.')
                l = -1
            if pattern[i] == '*':
                if pattern[i - 1] == '.':
                    del pattern_list[-1]
                    pattern_list.append('.*')
                else:
                    pattern_list.append(pattern[i - l:i - 1])
                    pattern_list.append(pattern[i - 1: i + 1])
                l = -1
            l = l + 1
        pattern_list.append(pattern[len(pattern) - l:])
        i = 0
        while i < len(pattern_list):
            if not pattern_list[i]:
                del pattern_list[i]
                i = i - 1
            i = i + 1
        i = 0
        j = 0
        while j < len(pattern_list) and i < len(s):
            if len(pattern_list[j]) == 2 and pattern_list[j][1] == '*':
                if pattern_list[j][0] == '.':
                     char = s[i]
                else:
                    char = pattern_list[j][0]
                while i < len(s) and s[i] == char:
                    i = i + 1
                j = j + 1
            elif pattern[j] == '.':
                i = i + 1
                j = j + 1
            else:
                if len(s) - i < len(pattern_list[j]):
                    return False
                elif s[i: i + len(pattern_list[j])] == pattern_list[j]:
                    j = j + 1
                    i = i + len(pattern_list[j - 1])
        if i == len (s) and j < len(pattern_list):
            for k in range(j, len(pattern_list)):
                if not (len(pattern_list[k]) == 2 and pattern_list[j][1] == '*'):
                    return False
            return True
        elif i < len(s) and j == len(pattern_list):
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    print(s.match('aaa', 'ab*ac*a'))


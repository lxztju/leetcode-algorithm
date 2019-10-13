# -*- coding:utf-8 -*-
# @time :2019.09.11
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


class Solution:
    def shortestToChar(self, S: str, C: str):

        prev = float('-inf')
        result = []
        for i, s in enumerate(S):
            if s == C:
                prev = i

            result.append(i - prev)


        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            result[i] = (min(result[i], prev - i))
        return result

S = Solution()
print(S.shortestToChar('fjhgiufghiuhd','f'))
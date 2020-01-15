# -*- coding:utf-8 -*-
# @time :2019/12/7
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

###BFS

class Solution:
    def numSquares(self, n: int) -> int:

        if n == 0: return 0
        #建立队列
        from collections import deque
        q = deque()

        q.append(n)
        step = 0

        #避免重复进行读取扫描
        visited = set()

        while q:
            step += 1
            # print(step)
            # print(q)
            for  _ in range(len(q)):
                ###将队列中元素出战
                temp = q.popleft()
                max_num = int(temp **0.5)

                ##找到与这一个节点相链接的下一个节点，并将下一个节点入队列
                for i in range(1, max_num + 1, 1):
                    diff = temp - i ** 2
                    if diff == 0:
                        return step
                    if diff not in visited:
                        q.append(diff)
                        visited.add(diff)

        return step
# -*- coding:utf-8 -*-
# @time :2019/11/23
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

class Solution:
    def maxPoints(self, points) -> int:
        from collections import Counter, defaultdict
        # 所有点统计
        points_dict = Counter(tuple(point) for point in points)
        # 把唯一点列举出来
        not_repeat_points = list(points_dict.keys())
        n = len(not_repeat_points)
        if n == 1: return points_dict[not_repeat_points[0]]
        res = 0
        # 求最大公约数
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        for i in range(n - 1):
            # 点1
            x1, y1 = not_repeat_points[i][0], not_repeat_points[i][1]
            # 斜率
            slope = defaultdict(int)
            for j in range(i + 1, n):
                # 点2
                x2, y2 = not_repeat_points[j][0], not_repeat_points[j][1]
                dy, dx = y2 - y1, x2 - x1
                # # 方式一 利用公约数
                # g = gcd(dy, dx)
                # if g != 0:
                #     dy //= g
                #     dx //= g
                # slope["{}/{}".format(dy, dx)] += points_dict[not_repeat_points[j]]
                # --------------------
                # 方式二, 利用除法(不准确, 速度快)
                if dx == 0:
                    tmp = "#"
                else:
                    tmp = dy * 1000 / dx * 1000
                slope[tmp] += points_dict[not_repeat_points[j]]
                #------------------------------
            res = max(res, max(slope.values()) + points_dict[not_repeat_points[i]])
        return res

s = Solution()
points =  [[1,1],[1,1],[2,3]]
res = s.maxPoints(points)
print(res)
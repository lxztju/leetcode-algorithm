# -*- coding:utf-8 -*-
# @time :2019/11/23
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) 
# 其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
# 找到所有回旋镖的数量
# 可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。


#查找表法：将距离作为键值，统计每个距离的个数

class Solution:
    def numberOfBoomerangs(self, points) -> int:

        res = 0

        if not points or len(points)<3:
            return res

        from collections import defaultdict
        for i in range(len(points)):

            dist_dict = defaultdict(int)

            for j in range(len(points)):
                dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                # print(dist)
                dist_dict[dist] += 1
            # print(dist_dict)
            for v in dist_dict.values():
                if v > 1:
                    res += (v*(v-1))

        return res

s = Solution()
points = [[0,0],[1,0],[2,0]]
res = s.numberOfBoomerangs(points)
print(res)
# -*- coding:utf-8 -*-
# @time :2019/10/13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水


### 对撞指针
# 面积取决于宽度，高度的最小值
# 刚开始去头尾令，宽度最大，然后限制面积的高度较小的指针移动去找寻更高的高度，以此获得更大的面积

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # 利用对撞指针
        p1 = 0  # 首指针
        p2 = len(height) - 1  # 尾指针
        max_area = -1  # 面积的最大值
        _width = 0

        while p1 < p2:

            _width = p2 - p1
            if height[p1] > height[p2]:
                _height = height[p2]
                p2 -= 1
            else:
                _height = height[p1]
                p1 += 1
            maxarea = _width * _height
            if maxarea >= max_area:
                max_area = maxarea

        return max_area

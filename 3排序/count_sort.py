# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

## 计数排序
# 统计每个数字出现的次数，然后进行重新赋值，完成排序
# 时间复杂度：平均O(n+k), 最坏O(n+k), 最好O(n+k)
# 稳定


def CountSort(nums):
    bucket = [0] * (max(nums) + 1) # 桶的个数
    for num in nums:  # 将元素值作为键值存储在桶中，记录其出现的次数
        bucket[num] += 1
    i = 0  # nums 的索引
    for j in range(len(bucket)):
        while bucket[j] > 0:
            nums[i] = j
            bucket[j] -= 1
            i += 1


if __name__ == "__main__":
    numbers = [1,1,1,1,2,2,2,2,2,5,5,5,5]
    CountSort(numbers)
    print(numbers)
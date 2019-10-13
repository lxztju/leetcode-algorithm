# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

##桶排序
# 计数排序的升级版，采用桶映射函数
# 将数组中最大值与最小值中间的元素，放置在对应的桶中，然后对于每个桶中的元素进行排序
# 映射函数的选取，影响了性能，尽可能均匀的将元素放置在桶中
# 最好的情况：均匀放置，最差的情况：所有数据放置在一个桶中
# 时间复杂度：平均O(n+k), 最坏O(n^2), 最好O(n)
# 稳定


from quick_sort import QuickSort

def BucketSort(nums, defaultBucketSize = 100):
    """
    桶排序
    :param nums: 输入的待排序数组
    :param defaultBucketSize: 桶数目，不指定时为5
    :return: inplace 操作
    """
    maxVal, minVal = max(nums), min(nums)

    bucketSize = defaultBucketSize  # 如果没有指定桶的大小，则默认为5

    bucketCount = ((maxVal - minVal) // bucketSize) + 1  # 数据分为 bucketCount 组

    buckets = []  # 二维桶

    for i in range(bucketCount):
        buckets.append([])

    # 利用函数映射将各个数据放入对应的桶中
    for num in nums:
        buckets[(num - minVal) // bucketSize].append(num)

    nums.clear()  # 清空 nums
    # print(buckets)

    # 对每一个二维桶中的元素进行排序
    for bucket in buckets:
        QuickSort(bucket)  # 使用快速排序

        nums.extend(bucket)    # 将排序好的桶依次放入到 nums 中
        # print(nums)


if __name__ == "__main__":
    numbers = [12, 321, 432, 5, 43, 6, 45, 765, 7, 65, 876, 8, 67, 98, 679, 87, 987, 9]
    BucketSort(numbers)
    print(numbers)

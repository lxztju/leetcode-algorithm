# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju





##归并排序
# 分而治之的思想
# step1 分解：将原问题分解为若干个规模较小，相互独立，与原问题形式相同的子问题；
# step2 解决：若子问题规模较小而容易被解决则直接解，否则递归地解各个子问题
# step3 合并：将各个子问题的解合并为原问题的解。
# 将原始数组逐渐一分为二，直到不能拆分，最终得到单元素即为已经排序，然后进行合并两个已排序的子序列
# 时间复杂度：平均O(nlogn), 最坏O(nlogn), 最好O(nlogn)
# 稳定

#利用递归来实现拆分

def Merge(left, right):
    """
    合并两个已排序子序列
    :param left: 第一个已排序的子序列
    :param right: 第二个已排序的子序列
    :return:  合并后的排序序列
    """
    i = 0
    j = 0
    result = []
    length_left = len(left)
    length_right = len(right)

    while i < length_left and j < length_right:
        # 逐个比较两个列表的元素
        # 小的添加进新列表，大的留下继续比较
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 最后加上未比较的元素
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def MergeSort(numbers):
    """
    归并排序算法入口，采用递归拆分列表
    :param numbers: 输入待排序数组
    :return:  排序后的数组
    """
    # 递归退出条件判断
    length = len(numbers)
    if length <= 1:
        return numbers

    # 递归拆分，取整
    mid = length // 2
    left = MergeSort(numbers[:mid])
    right = MergeSort(numbers[mid:])

    # 合并排序（归并排序）
    return Merge(left, right)


if __name__ == "__main__":
    numbers = [12,321,432,5,43,6,45,765,7,65,876,8,67,98,679,87,987,9,4345325]

    print(MergeSort(numbers))
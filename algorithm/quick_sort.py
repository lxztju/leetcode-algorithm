# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

## 快速排序
# 分而治之思想
# 类似于归并排序
# 首先找到一个基准值，一般将序列的第一个元素作为基准值
# 将比基准值小的元素均放置在基准值左边，大于基准值的放置在右边
# 然后递归处理左边与右边的序列

# 时间复杂度：平均O(nlogn), 最坏O(nlogn), 最好O(nlogn)
# 不稳定

def QuickSort(numbers):
    """
    快速排序的入口程序
    :param numbers:输入待排序的序列
    :return:
    """
    l = 0
    r = len(numbers)-1
    quick_sort(numbers, l, r)


def quick_sort(array, l, r):
    """
    快速排序的主程序
    :param array: 待排序的序列
    :param l: 序列最左端的元素指针
    :param r: 序列最右端的元素指针
    :return: in—place操作
    """
    if l < r:
        p = partition(array, l, r)
        quick_sort(array, l, p-1)
        quick_sort(array, p+1, r)


def partition(array, l, r):
    """
    分片操作，将未排序的数组按照与基准值的大小关系分割为左右两部分。
    采用双指针， i（慢指针）指向写入比基准值大的元素的位置，j（快指针）遍历数组
    :param array:  输入未排序的数组
    :param l: 序列的最左端指针
    :param r:  序列的最右端指针
    :return: 返回基准值的放置位置
    """
    x = array[l]  #基准值为序列最左边的值
    i =  r + 1   # 慢指针，指向大于基准值的元素的写入地址

    for j in range(r ,  l-1 , -1):

        ## 将小于基准值的元素，交换至i指向的地址
        if array[j] > x:
            i -= 1
            array[i], array[j] = array[j], array[i]

    array[i - 1], array[l] = array[l], array[i - 1]
    return i -1


if __name__ == "__main__":
    numbers = [5,6,7,8,54354,65,7,65,7,65,8,768,76,9]
    QuickSort(numbers)
    print(numbers)

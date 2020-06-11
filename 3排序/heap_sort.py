# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


##堆排序
# 进行升序排序构建大根堆，然后将堆顶元素与堆的最后一个元素交换，然后去掉最后一个堆元素，
# 将剩下的堆部分，重新构建大根堆，然后进行交换，直至堆只剩一个元素
#时间复杂度：平均O(nlogn), 最坏O(nlogn), 最好O(nlogn)
#稳定

heap_size = 0
LEFT = lambda i : 2 * i + 1
RIGHT  = lambda i : 2 * i + 2

def HeapSort(nums):
    """
    堆排序，进行升序排列
    :param nums: 输入的数组序列
    :return: inplace 操作
    """
    global heap_size
    BuildMaxHeap(nums)
    for i in range(len(nums)-1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heap_size -= 1
        KeepHeap(nums, 0)



def BuildMaxHeap(nums):
    """
    构建最大堆，将数组nums构建为最大堆
    :param nums: 输入的数组
    :return: in_place操作
    """
    global heap_size
    heap_size = len(nums)
    # print(heap_size)
    for i in range(len(nums)//2-1, -1, -1):
        KeepHeap(nums, i)


def KeepHeap(nums, i):
    """
    维护最大堆，比较第i个节点的左右字节点的大小关系并进行交换
    :param nums: 输入待构建最大堆的数组
    :param i: 第i个堆节点元素
    :return: in_place 操作
    """
    l, r = LEFT(i), RIGHT(i)
    # print(heap_size)
    largest = l if l < heap_size and nums[l] > nums[i] else i
    largest = r if r < heap_size and nums[r] > nums[largest] else largest

    if i != largest:
        nums[i],  nums[largest] = nums[largest], nums[i]
        KeepHeap(nums, largest)


if __name__ == "__main__":
    numbers = [1, 5, 9, 10, 11, 13, 12, 13, 15]
    HeapSort(numbers)
    # BuildMaxHeap(numbers)
    print(numbers)
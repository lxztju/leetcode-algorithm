# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

import random
import time
import sys
sys.setrecursionlimit(10000000)  #设置递归深度

from bubble_sort import BubbleSort
from insert_sort import InsertSort, ShellSort
from select_sort import SelectSort
from heap_sort import HeapSort
from quick_sort import QuickSort
##归并排序有返回值，其他的都是inplace操作
from merge_sort import MergeSort
from bucket_sort import BucketSort
from count_sort import CountSort
from radix_sort import RadixSort

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

numbers = random_int_list(1, 10000, 10000)

func_dict = {
    0: BubbleSort,
    1: InsertSort,
    2: ShellSort,
    3: SelectSort,
    4: QuickSort,
    5: HeapSort,
    6: BucketSort,
    7: CountSort,
    8: RadixSort
}
for num in range(9):
    func = func_dict.get(num)

    t1 = time.time()
    func(numbers)
    t2 = time.time()
    print("time: ", t2-t1)


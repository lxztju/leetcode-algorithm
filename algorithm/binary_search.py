# -*- coding:utf-8 -*-
# @time :2019.10.10
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju


#二分查找

def binary_search(array,target):
    """
    binary search
    :param array:sorted number array
    :param target: target number
    :return: target index in array, if find nothing return None
    """
    left = 0
    right = len(array) - 1

    while left <= right:

        mid = (left + (right-left)// 2)



        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

array = [1,2,3,4,5,6,7]
target = 3

print(binary_search(array,target))
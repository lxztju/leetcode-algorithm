# -*- coding:utf-8 -*-
# @time :2019.10.10
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


#二分查找

def BinarySearch(array,target):
    """
    binary search，在两个边界，[left, right]中搜寻目标值
    :param array:sorted number array
    :param target: target number
    :return: target index in array, if find nothing return None
    """
    left = 0   #左侧边界
    right = len(array) - 1  #右侧边界

    while left <= right:  #在闭合区间中找寻结果目标值[0,n-1]

        mid = (left + (right-left)// 2)   #放置数值越界

        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7]
    target = 3

    print(BinarySearch(array,target))
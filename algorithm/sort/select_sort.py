# -*- coding:utf-8 -*-
# @time :2019.10.12
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

##选择排序
# 数组分为前端已排序数组，尚未排序的序列，每次找到未排序序列的最小值放置在未排序序列的开头
# 未排序序列变短，直到完全排序

#时间复杂度：平均O(n^2), 最坏O(n^2), 最好O(n^2),(最差的排序，一般不使用）
#不稳定

def SelectSort(numbers):

    min_num = float("inf") #用于存储子序列的最小数组元素索引
    min_index = -1

    # 外层循环控制遍历数组序列,也就是表示已排序数组的末尾元素
    for i in range(len(numbers)-1):

        # 找出未排序子序列的最小元素并放置在开头
        for j in range(i, len(numbers)):
            if numbers[j] < min_num:
                min_num = numbers[j]
                min_index = j

        numbers[i],numbers[min_index] = numbers[min_index], numbers[i]
        #print(numbers)
        min_num = float("inf")



if __name__ == "__main__":
    numbers = [12, 321, 432, 5, 43, 6, 45, 765, 7, 65, 876, 8, 67, 98, 679, 87, 987, 9, 4345325]
    SelectSort(numbers)
    print(numbers)
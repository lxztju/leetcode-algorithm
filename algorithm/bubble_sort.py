# -*- coding:utf-8 -*-
# @time :2019.10.12
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


#冒泡排序

#利用双层循环，外层循环控制比较的次数，内层循环控制交换归位数据
#时间复杂度：平均O(n^2), 最坏O(n^2), 最好O(n)
#稳定的排序算法

def BubbleSort(numbers):

    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1) :
            if numbers[j] > numbers[j + 1] :
                numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]




if __name__ == "__main__":
    numbers = [12, 321, 432, 5, 43, 6, 45, 765, 7, 65, 876, 8, 67, 98, 679, 87, 987, 9, 4345325]
    BubbleSort(numbers)
    print(numbers)
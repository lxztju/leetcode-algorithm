# -*- coding:utf-8 -*-
# @time :2019.10.12
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



####插入排序
#第i个元素左边的元素已经排序，将第i个元素与前边的已排序序列进行比较，并交换
#遍历整个数组，完成排序

#时间复杂度：平均O(n^2), 最坏O(n^2), 最好O(n)
#稳定的排序算法

def InsertSort(numbers):

    for i in range(len(numbers)): ##外层循环控制遍历数组
        #内层循环控制比较与交换
        for j in range (i):
            #第i个元素比之前的元素小，进行交换
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]




##插入排序升级版——希尔排序
# 等间隔取元素组成子序列进行排序，间隔逐渐变小，序列的长度逐渐曾长
# 如果所取的间隔互相不互质，那么小间隔的一部分序列则不起作用，效果变坏
#时间复杂度：平均O(n^1.3), 最坏O(n^2), 最好O(n)
#不稳定
def ShellSort(numbers):

    def insert(nums, d):
        """
        对子序列进行插入排序
        :param nums: 需要排序的序列
        :param d: 抽取子序列的间隔
        :return: 对子序列排序后的序列
        """
        for i in range(len(nums)//d):
            for j in range(i):
                back = i * d
                forward = j * d
                if nums[back] < nums[forward]:
                    nums[back], nums[forward] = nums[forward], nums[back]

        return nums

    d = len(numbers) //2
    while d >=1:
        numbers = insert(numbers, d)
        d = d //2




if __name__ == "__main__":
    numbers = [12, 321, 432, 5, 43, 6, 45, 765, 7, 65, 876, 8, 67, 98, 679, 87, 987, 9, 4345325]
    InsertSort(numbers)
    ShellSort(numbers)
    print(numbers)

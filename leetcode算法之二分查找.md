今天来盘一盘 ** 二分查找 ** 这类题目


代码采用**C++**实现

使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)



## 二分查找
二分查找是针对一个排序列表,每次利用中间元素折半去掉部分元素,减少重复的查找遍历.

* 对于一个排序数组nums,查找指定的一个数字target,采用二分查找的解题思路
* 利用target与nums数组的中间元素相比较,
	1. 如果target> nums[mid],说明target在数组的后半部分,
	2. 如果target < nums[mid],  说明target在数组的前半部分
	3. 如果target == nums[mid], 找到target.

二分查找的典型解题思路模板代码:

```c++
int binary_search(vector<int>& nums, int target){
	int l = 0, r = nums.size() - 1;
	while (l <= r){
		int mid = l + (r - l) / 2;  // 直接采用(r+l)/2. 容易出现整形溢出
		// 找到对应的元素,返回索引
		if (nums[mid] == target) return mid;
		// target比中间值大,说明存在数组后半部分
		else if (nums[mid] < target)
			l = mid + 1;
		// target小, 说明存在数组的前半部分.
		else
			r = mid - 1;
	}
	return -1;
}
```

**两个非常困扰而且易错的细节点:**
* while循环的判断条件是`l<r`还是`l<=r`
* 当target != nums[mid]时, 使用`mid`还是`mid (+或者-) 1`

解决这两个问题的只需要考虑清楚,**查找区间的封闭情况**, 例如对于上边写的代码,采用的方式为(**左右均为闭区间**)[l, r],  因此决定了循环判断条件为`l<=r`. 同时 `l = mid + 1`与`r = mid - 1`, 在过程中**始终保持全闭区间的情况不变**

当然代码也可以采用左开右闭或者左闭右开的区间进行查找,然后判断需要如何更改这两个问题.

* 69 x 的平方根 (Easy)
* 744 寻找比目标字母大的最小字母   (Easy)
* 278 第一个错误的版本   (Easy)
* 540 有序数组中的单一元素   (Medium)
* 153 	寻找旋转排序数组中的最小值   (Medium)
* 34 在排序数组中查找元素的第一个和最后一个位置(medium)



#### 69 x 的平方根 (Easy)
* 题解: 二分查找
	* 全闭区间进行搜索
	* 注意在计算过程中,直接平方会导致int溢出,需要转换为double,或者long long

```c++
class Solution {
public:
    int mySqrt(int x) {
        // 采用二分查找
        // 查找区间为[l, r]
        int l=0, r=x/2;
        while (l <= r){
            int mid = l + (r - l) / 2;
            double pow1 = static_cast<double>(mid) * mid;
            double pow2 = static_cast<double>(mid + 1) * (mid + 1);
            if (pow2 == x) return mid + 1;
            else if (pow1 == x || (pow1 < x && pow2 > x)) return mid;
            else if (pow1 > x)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return l;
    }
};
```


#### 744 寻找比目标字母大的最小字母   (Easy)

```c++
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        if (target >= *(letters.end() - 1)) return *(letters.begin());
        // 全闭区间
        int l = 0, r = letters.size() - 1;
        while (l <= r){
            int mid = l + (r - l) / 2;
            if (target < letters[mid])
                r = mid - 1;
            else if (target >= letters[mid])
                l = mid + 1;
        }
        return letters[l];
    }
};
```
#### 278 第一个错误的版本   (Easy)
```c++
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        // 直接二分即可,找到第一个为false的版本
        // 全闭区间
        int l = 1, r = n;
        while (l <= r){
            int mid = l + (r - l) /2 ;
            if (isBadVersion(mid))
                r = mid - 1;
            else
                l = mid + 1;
        }
        return l;
    }
};
```

#### 540 有序数组中的单一元素   (Medium)

* 题解: 二分查找
	* 这道题直接判断中间元素左右两侧的子数组哪一部分是奇数,说明单一元素就存在对应的部分
	* 如果mid后半部分的数组是偶数:
	* 1. 那么如果mid与mid+1位置的元素相等, 那么去掉这俩元素后,后半部分就是奇数,说明单一元素存在右半部分, l = mid + 2
	* 2. 如果mid与mid - 1位置相等,那么单一元素存在左半部分, r = mid - 2
	* 同理分析mid的后半部分是奇数.
	* 如果两侧均为偶数,那么mid即为待查找的单一元素.


```c++
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        // 二分查找
        // mid为数组中间的元素索引
        // 如果mid与后边或者前边的元素相等, 那么判断哪一侧是奇数就说明在哪一侧
        // 如果mid刚好就是单独的元素,那么直接返回即可
        int l = 0, r = nums.size() - 1;
        while (l < r){
            int mid = l + (r - l) / 2;
            // 后半部分是偶数
            bool second_even = ((r - mid) % 2 == 0);

            if (nums[mid + 1] == nums[mid]){
                if (second_even)
                    l = mid + 2;
                else
                    r = mid - 1;
            }
            else if (nums[mid] == nums[mid - 1]){
                if (second_even)
                    r = mid - 2;
                else
                    l = mid + 1;
            }
            else
                return nums[mid];
        }
        return nums[l];
    }
};
```


#### 153 	寻找旋转排序数组中的最小值   (Medium)
* 题解1: 简单顺序查找
	* 遍历数组, 如果nums[i] > nums[i+1] return num[i+1]
	* 如果遍历完全没有找到,就说明nums[0]是最小的元素.


```c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        // 顺序查找, 如果前边元素,大于后边,那么就找到了对应的元素
        for (int i = 0; i < nums.size() - 1; i++){
            if (nums[i] > nums[i+1])
                return nums[i+1];
        }
        return nums[0];
    }
};
```

* 题解2: 二分查找
	* 采用中间元素与首尾元素进行对比的方式
	* 如果中间元素大于数组尾元素,说明反转点在mid的右边
	* 如果中间元素小于数组的尾部元素. 说明反转点在mid或者在mid的左边

```c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {          
                left = mid + 1;
            } else {                               
                right = mid;
            }
        }
        return nums[left];
    }
};
```


#### 34 在排序数组中查找元素的第一个和最后一个位置(medium)

* 题解: 顺序查找

```c++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        // 直接顺序查找
        int l = 0, r = nums.size() - 1;
        vector<int> res;
        while (l <nums.size() && nums[l] != target)
            l++;
        while (r > 0 && nums[r] != target )
            r--;
        if (l != nums.size())
            return {l, r};
        else
            return {-1, -1};
    }
};
```

* 题解2: 二分查找
	* 首先利用二分查找,找到对应的target
	* 然后顺序往左右扩展找到对应的边界

```c++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        // 使用二分查找,找到对应元素, 然后左右遍历得到两个坐标
        int index = -1;
        while (l <= r){
            int mid = l + ( r - l ) / 2;
            //找到对应的元素索引
            if (nums[mid] == target){
                index = mid;
                break;
            }
            else if(nums[mid] < target)
                l = mid + 1;
            else
                r = mid - 1;
        }
		// 没有找到对应的索引
        if (index == -1) 
            return {-1, -1};

        int left = index, right = index;
        // 向左扩展,找到元素左边界
        while (left >= 0 && nums[left] == target )
            left--;
        // 向右扩展找到有边界
        while (right < nums.size() && nums[right] == target)
            right++;
        return {left + 1, right - 1};
    }
};
```





## 更多分类刷题资料

* 微信公众号： 小哲AI

  ![wechat_QRcode](https://img-blog.csdnimg.cn/20210104185413204.jpg)

* GitHub地址： [https://github.com/lxztju/leetcode-algorithm](https://github.com/lxztju/leetcode-algorithm)
* csdn博客： [https://blog.csdn.net/lxztju](https://blog.csdn.net/lxztju)
* 知乎专栏： [小哲AI](https://www.zhihu.com/column/c_1101089619118026752)
* AI研习社专栏：[小哲AI](https://www.yanxishe.com/column/109)


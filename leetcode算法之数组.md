明年就是找工作了，又要开始刷题了，把之前做过的题目再梳理整理一遍，但愿明年不要那么拉跨，祈祷明年能找到工作，千万不能毕业就失业。

分类别解析leetcode上的一些相关的例题路，代码采用**C++与python**实现。

所有的题目均来自leetcode官网.

## 数组

涉及的一些leetcode问题：

* 283 Move Zeroes (Easy)
* 566 Reshape the Matrix (Easy)
* 485 Max Consecutive Ones (Easy)
* 240 Search a 2D Matrix II (Medium)
* 378 Kth Smallest Element in a Sorted Matrix ((Medium))
* 645 Set Mismatch (Easy)
* 287 Find the Duplicate Number (Medium)
* 697 Degree of an Array (Easy)
* 766 Toeplitz Matrix (Easy)
* 565 Array Nesting (Medium)


####  283 Move Zeroes (Easy)

> 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
> 
> 说明:
> 
> 		必须在原数组上操作，不能拷贝额外的数组。
> 		尽量减少操作次数。

* 第一个直观的想法:
使用额外的数组,直接遍历一遍原始数组,然后将非零的复制到前半部分,在后边按照数组补零即可.

```c++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
    // 新建一个vector,保存移动后的vector
        vector<int> res(nums.size(), 0);
        int j = 0;
        // 遍历原始数组,修改res中的元素
        for (int i=0; i < nums.size(); i++){
            if (nums[i]!=0){
                res[j] = nums[i];
                j++;
            }
        }
        // 将res再赋值给原始数组
        nums.assign(res.begin(), res.end());
    }
};
```

* 题目要求不能使用额外的数组.
就只能使用双指针在原始数组上操作,左指针指向交换完成的元素,右指针向后扫描查找交换元素

```c++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // 双指针
        int l=0, r=0;

        while (r < nums.size()){
            if (nums[r] != 0){
                swap(nums[r], nums[l]);
                l++;
            }
            r++;
        }
    }
};
```


####  566 Reshape the Matrix (Easy)
题目较简单,直接附上代码,遍历即可

```c++
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        // 直接遍历即可
        int m=nums.size(), n=nums[0].size();
        if (m*n != r*c) return nums;
        vector<vector<int>> res(r, vector<int>(c, 0)); //保存最终的结果
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                int index = i*n + j;
                res[index/c][index%c] = nums[i][j];
            }
        }
        return res; 
    }
};
```

####  485 Max Consecutive Ones (Easy)
```c++
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        //直接遍历
        int res = 0;
        int i = 0;
        while (i < nums.size()){
            int count = 0;
            while (i < nums.size() && nums[i] == 1){
                count++;
                i++;
            }
            res = max(res, count);
            i++;
        }
        return res;
    }
};
```

####  240 Search a 2D Matrix II (Medium)

>编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
> 
> 每行的元素从左到右升序排列。
>  每列的元素从上到下升序排列。

* 最直观的想法, 直接遍历二维数组进行对比,这就变成了一道简单题,没有用到题目当中的条件

* 从右上角开始遍历,因为这样遍历,比target小的在左边,比target大的在下边

```c++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // 从右上角开始遍历
        int m = matrix.size(), n = matrix[0].size();
        int i = 0, j = n-1;
        while (i >= 0 && i < m && j >= 0 && j < n){
                if (matrix[i][j] == target) 
                    return true;
                else if (matrix[i][j] > target)
                    j--;
                else 
                    i++;
        }
        return false;
    }
};
```


####  378 Kth Smallest Element in a Sorted Matrix ((Medium))
> 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。

* 第一个思路: 直接将其变为一维数组,然后直接进行排序,找到第k小的元素.

```c++
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> res(m*n, 0);
        int index = 0;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                res[index] = matrix[i][j];
                index++;
            }
        }
        sort(res.begin(), res.end());
        return res[k-1];
    }
};
```



* 第二个思路,利用优先级队列.
* 
将所有的元素全部插入优先级队列中,然后找到第k个
```c++
class point{
    public:
        int val, x, y;
        point()=default;
        point(int val, int x, int y): val(val), x(x), y(y) {}
        bool operator > (const point& a) const {
            return this->val > a.val;
        }
};

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        //按行进行归并排序
        //定义优先级队列,这个队列采用vector实现
        priority_queue<point, vector<point>, greater<point>> q;
        int n = matrix.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
            q.emplace(point(matrix[i][j], i, j));
        }
        point res;
        for (int i = 0; i < k - 1; i++) {
            res = q.top();
            q.pop();
        }
        return q.top().val;
    }
};
```

插入的时候不需要将所有的元素均插入,按照其升序的特点,只需要按行插入右侧元素即可,找到最小的k个

```c++
class point{
    public:
        int val, x, y;
        point()=default;
        point(int val, int x, int y): val(val), x(x), y(y) {}
        bool operator > (const point& a) const {
            return this->val > a.val;
        }
};

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        //按行进行归并排序
        //定义优先级队列,这个队列采用vector实现
        priority_queue<point, vector<point>, greater<point>> q;
        int n = matrix.size();
        for (int i = 0; i < n; i++) {
            q.emplace(point(matrix[i][0], i, 0));
        }
        for (int i = 0; i < k - 1; i++) {
            point now = q.top();
            q.pop();
            if (now.y != n - 1) {
                q.emplace(matrix[now.x][now.y + 1], now.x, now.y + 1);
            }
        }
        return q.top().val;
    }
};
```

####  645 Set Mismatch (Easy)

> 集合 S 包含从1到 n的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
> 
> 给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

非常简单的题目, 直接使用哈希表即可,找出哪一个数字已经出现过,然后查找那个数字没有出现过,共遍历两次.

```c++
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> res;
        unordered_set<int> hashset;
        for (auto c : nums){
            if (hashset.find(c) == hashset.end())
                hashset.insert(c);
            else 
                res.push_back(c);
        }
        for (int i=1; i <= nums.size(); i++){
            if (hashset.find(i) == hashset.end())
                res.push_back(i);
        }
        return res;
    }
};
```


####  287 Find the Duplicate Number (Medium)

> 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和n），
> 可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

直观的几种想法:
* 直接遍历,两重循环,每次查找元素nums[i]是否在nums[i+1:]的范围内出现,时间复杂度n2,不满足题意
* hash表存储访问过的元素,空间复杂度o(n),不满足题意
* 先排序,然后遍历相邻的相同元素即为重复元素,不满足"不能更改原数组"的要求.

这道题的限制条件,直接堵死了常用的几种直观的思路.

这里采用**二分查找**来解决这个问题.

> 题解:
> 1. 这道题的数字的范围均在1~n之间,且只有一个重复的数.举个例子就知道
> 例如  [1,3,4,2,2], n=4,因此设置mid = (1+4) / 2=2, 那么小于等于2的数字有3个大于选定的mid,因此重复的数字就肯定小于等于mid,否则重复的数字大于mid

```c++
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size()-1;
        int l= 0, r = n;
        // 二分法查找区间
        while (l < r){
            int mid = l + (r - l) / 2;
            int cnt = 0;
            // 统计小于等于mid的数字的数目
            for (auto num :nums){
                if (num <= mid)
                    cnt++;
            }
            // 如果统计的数字大于mid,那么最终重复的数字位于左侧
            if (cnt > mid)
                r = mid;
            else
                l = mid+1;
        }
        return l;
    }
};
```

####  697 Degree of an Array (Easy)

> 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
> 
> 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

简单的题目,但是注意频数最大的数组元素不一定只有一个

```c++
#include <algorithm>

class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        // 使用无序映射表来存储每个元素在数组中出现的索引列表
        unordered_map<int, vector<int>> res;
        for (auto e : nums){
            res.insert(make_pair(e, vector<int>()));
        }

        for (int i=0; i <nums.size(); i++){
            res[nums[i]].push_back(i);
        }
        
        int min_dis = nums.size();
        int max_ferq = 0;
        // 查找出现最多的索引出现的次数
        for (auto e=res.cbegin(); e != res.end(); e++){
            vector<int> index = e->second;
            int dis = index.size();
            max_ferq = max(max_ferq, dis);
        }
        //统计最小的连续子数组
        for (auto e=res.cbegin(); e != res.end(); e++){
            vector<int> index = e->second;
            if (index.size() == max_ferq){
                min_dis = min(min_dis, index[index.size()-1] - index[0] + 1);
            }
        }
        return min_dis;
    }
};
```


####  766 Toeplitz Matrix (Easy)

> 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
> 
> 给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。

简单的题目, 仅仅需要发现`同一条对角线上的横纵坐标差值为常数(在做八皇后问题也会遇到)`就可以了,然后借助map可以轻松求解.

```c++
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        // 利用哈希表来,键为行列坐标的差值, 值为对应的数字
        unordered_map<int, int> indexdiff_value;
        for (int i = 0; i < matrix.size(); i++){
            for (int j = 0; j < matrix[0].size(); j++){
                if (indexdiff_value.find(i - j) == indexdiff_value.end())
                    indexdiff_value.insert(make_pair(i-j, matrix[i][j]));
                else{
                    if (matrix[i][j] != indexdiff_value[i-j])
                        return false;
                }
            }
        }
        return true;
    }
};
```

####  565 Array Nesting (Medium)

> 索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]],
> A[A[A[i]]], ... }且遵守以下的规则。
> 
> 假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]...
> 以此类推，不断添加直到S出现重复的元素。

看似复杂,其实只需要将所有的 这种嵌套的子列全部查找出来,并找到最长的满足条件的最长的长度即可.

> 例如,对于[5,4,0,3,1,6,2]这个序列,其满足条件的S分别为: [5, 6, 0, 2], [4,1]与[3]这三个从中找到最短的即可.

基本办法就是遍历+ hash表去重

```c++
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        //利用哈希表记录访问过的元素,避免重复访问.
        unordered_set<int> visited;

        int res = 0; // 最终的结果,最长的S
        // 遍历,找到所有的字串
        for (int i = 0; i < nums.size(); i++){
            if( visited.find(nums[i]) != visited.end() ) continue;

            int length = 1;  // S的长度
            // 开始查找一个满足条件的S.
            int index = i;
            while (nums[index] != i){
                visited.insert(nums[index]);
                index = nums[index];
                length++;
            }
            visited.insert(nums[i]);
            res = max(res, length);
        }
        return res;
    }
};
```


## 更多笔记资料

* 微信公众号: 小哲AI

![wechat_QRcode](images/wechat_QRcode.jpg)
* GitHub地址： [https://github.com/lxztju/leetcode-algorithm](https://github.com/lxztju/leetcode-algorithm)
* csdn博客： [小哲AI](https://blog.csdn.net/lxztju)
* 知乎专栏： [小哲AI](https://www.zhihu.com/column/c_1101089619118026752)
* AI研习社专栏：[小哲AI](https://www.yanxishe.com/column/109)







